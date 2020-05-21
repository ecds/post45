import csv
from django.db import models
from django.views.generic import View
from django.http import StreamingHttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from htrc_features import utils


def index(request):
    return render(request, 'app/index.html')

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Record.objects.all().order_by('inferreddate')
    serializer_class = RecordSerializer

# def htrc_download(request, docid):
#     link = utils.download_file(htids='docid')
#     return render(request)



# https://docs.djangoproject.com/en/3.0/howto/outputting-csv/#streaming-large-csv-files
# http://blog.aeguana.com/2015/12/12/csv-export-data-for-django-model/
class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

class RecordExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs = Record.objects.all()
        model = records_qs.model
        model_fields = model._meta.fields + model._meta.many_to_many
        headers = [field.name for field in model_fields] # Create CSV headers
        def get_row(obj):
            row = []
            for field in model_fields:
                if type(field) == models.ForeignKey:
                    val = getattr(obj, field.name)
                    if val:
                        val = val.__unicode__()
                elif type(field) == models.ManyToManyField:
                    val = u', '.join([item.__unicode__() for item in getattr(obj, field.name).all()])
                elif field.choices:
                    val = getattr(obj, 'get_%s_display'%field.name)()
                else:
                    val = getattr(obj, field.name)
                #row.append(str(val).encode("utf-8"))
                row.append(str(val)) # Doing it this way removes enclosing quotes and preceding "b" 
            return row
        def stream(headers, data): # Helper function to inject headers
            if headers:
                yield headers
            for obj in data:
                yield get_row(obj)
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer, delimiter="\t")
        response = StreamingHttpResponse(
            (writer.writerow(row) for row in stream(headers, records_qs)),
            content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="data.tsv"'
        return response

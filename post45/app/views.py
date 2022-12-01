import csv
from django.db import models
from django.views.generic import View
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Record, ProgramEraRecord, ProgramEraPeople, ProgramEraGraduations, MasterPrizeRecord, NYTFull, NYTTitle, NYTHathi, MLPWinners, MLPHathi
from .serializers import RecordSerializer, ProgramEraRecordSerializer, ProgramEraPeopleSerializer, ProgramEraGraduationsSerializer, MasterPrizeRecordSerializer, NYTFullSerializer, NYTTitleSerializer, NYTHathiSerializer, MLPWinnersSerializer, MLPHathiSerializer
from htrc_features import utils


def index(request):
    return render(request, 'app/index.html')

def programerarecord(request):
    return render(request, 'app/programerarecord.html')

def programerapeople(request):
    return render(request, 'app/programerapeople.html')

def programeragraduations(request):
    return render(request, 'app/programeragraduations.html')

@login_required(login_url='/accounts/login/')
def masterprize(request):
    return render(request, 'app/masterprize.html')

def nytfull(request):
    return render(request, 'app/nytfull.html')

def nyttitle(request):
    return render(request, 'app/nyttitle.html')

def nythathi(request):
    return render(request, 'app/nythathi.html')

def mlpwinners(request):
    return render(request, 'app/mlpwinners.html')

def mlphathi(request):
    return render(request, 'app/mlphathi.html')

def about(request):
    return render(request, 'app/about.html')

class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Record.objects.all().order_by('inferreddate')
    serializer_class = RecordSerializer

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

class ProgramEraRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProgramEraRecord.objects.all().order_by('date')
    serializer_class = ProgramEraRecordSerializer


class ProgramEraRecordExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  ProgramEraRecord.objects.all()
        model = records_qs.model
        model_fields = model._meta.fields + model._meta.many_to_many
        exclude_fields = ['subjects', 'geographics', 'genres', 'classifications']
        model_fields = [x for x in model_fields if x.name not in exclude_fields]
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
        response['Content-Disposition'] = 'attachment; filename="pephtrccorpusdata.tsv"'
        return response

class ProgramEraPeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProgramEraPeople.objects.all().order_by('person_id')
    serializer_class = ProgramEraPeopleSerializer

class ProgramEraPeopleExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  ProgramEraPeople.objects.all()
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
        response['Content-Disposition'] = 'attachment; filename="people.tsv"'
        return response

class ProgramEraGraduationsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProgramEraGraduations.objects.all().order_by('record_id')
    serializer_class = ProgramEraGraduationsSerializer

class ProgramEraGraduationsExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  ProgramEraGraduations.objects.all()
        model = records_qs.model
        model_fields = model._meta.fields + model._meta.many_to_many
        headers = [field.name for field in model_fields] # Create CSV headers
        def get_row(obj):
            row = []
            for field in model_fields:
                if type(field) == models.ForeignKey:
                    val = getattr(obj, field.name)
                    if val:
                        val = val.__str__()
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
        response['Content-Disposition'] = 'attachment; filename="graduations.tsv"'
        return response

class ProgramEraPeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProgramEraPeople.objects.all().order_by('person_id')
    serializer_class = ProgramEraPeopleSerializer

class ProgramEraPeopleExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  ProgramEraPeople.objects.all()
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
        response['Content-Disposition'] = 'attachment; filename="programerapeople.tsv"'
        return response

class MasterPrizeRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MasterPrizeRecord.objects.all().order_by('lastname')
    serializer_class = MasterPrizeRecordSerializer

class MasterPrizeRecordExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  MasterPrizeRecord.objects.all()
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
        response['Content-Disposition'] = 'attachment; filename="masterprize.tsv"'
        return response

class NYTFullViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NYTFull.objects.all().order_by('year')
    serializer_class = NYTFullSerializer

class NYTFullExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  NYTFull.objects.all()
        model = records_qs.model
        model_fields = model._meta.fields + model._meta.many_to_many
        exclude_fields = ['id',]
        model_fields = [x for x in model_fields if x.name not in exclude_fields]
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
        response['Content-Disposition'] = 'attachment; filename="nyt_full.tsv"'
        return response

class NYTTitleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NYTTitle.objects.all().order_by('id')
    serializer_class = NYTTitleSerializer

class NYTTitleExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  NYTTitle.objects.all()
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
        response['Content-Disposition'] = 'attachment; filename="nyt_titles.tsv"'
        return response

class NYTHathiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NYTHathi.objects.all().order_by('htid')
    serializer_class = NYTHathiSerializer

class NYTHathiExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  NYTHathi.objects.all()
        model = records_qs.model
        model_fields = model._meta.fields + model._meta.many_to_many
        exclude_fields = ['id',]
        model_fields = [x for x in model_fields if x.name not in exclude_fields]
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
        response['Content-Disposition'] = 'attachment; filename="hathi_volumes.tsv"'
        return response

class MLPWinnersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MLPWinners.objects.all().order_by('person_id')
    serializer_class = MLPWinnersSerializer

class MLPWinnersExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  MLPWinners.objects.all()
        model = records_qs.model
        model_fields = model._meta.fields + model._meta.many_to_many
        exclude_fields = ['id',]
        model_fields = [x for x in model_fields if x.name not in exclude_fields]
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
        response['Content-Disposition'] = 'attachment; filename="winnersandjudges.tsv"'
        return response

class MLPHathiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MLPHathi.objects.all().order_by('hathi_id')
    serializer_class = MLPHathiSerializer

class MLPHathiExportCsvView(View):
    def get(self, request, *args, **kwargs):
        records_qs =  MLPHathi.objects.all()
        model = records_qs.model
        model_fields = model._meta.fields + model._meta.many_to_many
        exclude_fields = ['id',]
        model_fields = [x for x in model_fields if x.name not in exclude_fields]
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
        response['Content-Disposition'] = 'attachment; filename="hathitrust_prizewinners.tsv"'
        return response

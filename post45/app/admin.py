from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, SliderNumericFilter
from .models import Record


class RecordResource(resources.ModelResource):

    class Meta:
        model = Record

class RecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RecordResource
    list_display = ('docid', 'title', 'author','inferreddate', 'latestcomp')
    search_fields = ('docid', 'title', 'author')
    #list_filter = (
    #     ('inferreddate', SliderNumericFilter),
    #     ('latestcomp', SliderNumericFilter),
    # )
admin.site.register(Record, RecordAdmin)

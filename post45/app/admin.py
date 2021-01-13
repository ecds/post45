from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, SliderNumericFilter
from .models import Record, ProgramEraRecord, ProgramEraPeople, ProgramEraGr


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


class ProgramEraRecordResource(resources.ModelResource):

    class Meta:
        model = ProgramEraRecord

class ProgramEraRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        resource_class = ProgramEraRecordResource
        list_display = ('docid', 'title', 'authors', 'date')
        search_fields = ('docid', 'title', 'authors', 'date')

admin.site.register(ProgramEraRecord, ProgramEraRecordAdmin)


class ProgramEraPeopleResource(resources.ModelResource):

    class Meta:
        model = ProgramEraPeople

class ProgramEraPeopleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProgramEraPeopleResource
    list_display = ('person_id', 'full_name', 'gender', 'country')
    search_fields = ('person_id', 'full_name', 'gender', 'country')

admin.site.register(ProgramEraPeople, ProgramEraPeopleAdmin)


class ProgramEraGraduationsResource(resources.ModelResource):

    class Meta:
        model = ProgramEraGraduations

class ProgramEraGraduationsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProgramEraGraduationsResource
    list_display = ('record_id', 'graduate_name', 'program', 'degree', 'thesis_title', 'genre')
    search_fields = ('record_id', 'graduate_name', 'program', 'degree', 'thesis_title', 'genre')

admin.site.register(ProgramEraGraduations, ProgramEraGraduationsAdmin)

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, SliderNumericFilter
from .models import Record, ProgramEraRecord, ProgramEraPeople, ProgramEraGraduations, MasterPrizeRecord, NYTFull, NYTTitle, NYTHathi, MLPWinners, MLPHathi


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
        list_display = ('id', 'title', 'author1_normalized', 'date')
        search_fields = ('id', 'title', 'author1_normalized', 'date')

admin.site.register(ProgramEraRecord, ProgramEraRecordAdmin)


class ProgramEraPeopleResource(resources.ModelResource):

    class Meta:
        model = ProgramEraPeople
        exclude = ('id',)
        import_id_fields = ['person_id']

class ProgramEraPeopleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProgramEraPeopleResource
    list_display = ('person_id', 'full_name', 'gender', 'country')
    search_fields = ('person_id', 'full_name', 'gender', 'country')

admin.site.register(ProgramEraPeople, ProgramEraPeopleAdmin)


class ProgramEraGraduationsResource(resources.ModelResource):

    class Meta:
        model = ProgramEraGraduations
        exclude = ('id',)
        import_id_fields = ['record_id']

class ProgramEraGraduationsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProgramEraGraduationsResource
    list_display = ('record_id', 'graduate_name', 'program', 'degree', 'thesis_title', 'genre')
    search_fields = ('record_id', 'graduate_name', 'program', 'degree', 'thesis_title', 'genre')

admin.site.register(ProgramEraGraduations, ProgramEraGraduationsAdmin)


class MasterPrizeRecordResource(resources.ModelResource):

    class Meta:
        model = MasterPrizeRecord

class MasterPrizeRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MasterPrizeRecordResource
    list_display = ('name', 'role', 'prize', 'year', 'genre', 'type', 'amount')
    search_fields = ('name', 'role', 'prize', 'year', 'genre', 'type', 'amount')

admin.site.register(MasterPrizeRecord, MasterPrizeRecordAdmin)


class NYTFullResource(resources.ModelResource):

    class Meta:
        model = NYTFull

class NYTFullAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = NYTFullResource
    list_display = ('year', 'week', 'rank', 'title_id', 'title', 'author')
    search_fields = ('year', 'week', 'rank', 'title_id', 'title', 'author')

admin.site.register(NYTFull, NYTFullAdmin)

class NYTTitleResource(resources.ModelResource):

    class Meta:
        model = NYTTitle

class NYTTitleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = NYTTitleResource
    list_display = ('id', 'title', 'author', 'year')
    search_fields = ('id', 'title', 'author', 'year', 'total_weeks', 'first_week', 'debut_rank', 'best_rank')

admin.site.register(NYTTitle, NYTTitleAdmin)

class NYTHathiResource(resources.ModelResource):

    class Meta:
        model = NYTHathi

class NYTHathiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = NYTHathiResource
    list_display = ('htid', 'title_id', 'title', 'author', 'year')
    search_fields = ('htid', 'title_id', 'title', 'author', 'year', 'first_week', 'debut_rank', 'best_rank')

admin.site.register(NYTHathi, NYTHathiAdmin)

class MLPWinnersResource(resources.ModelResource):

    class Meta:
        model = MLPWinners

class MLPWinnersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MLPWinnersResource
    list_display = ('person_id', 'full_name')
    search_fields = ('person_id', 'full_name', 'given_name', 'last_name', 'gender', 'elite_institution', 'graduate_degree', 'mfa_degree', 'iowa_mfa_person_id', 'stegner', 'role', 'prize_institution', 'prize_name', 'prize_year', 'prize_genre', 'prize_type', 'prize_amount', 'title_of_winning_book')

admin.site.register(MLPWinners, MLPWinnersAdmin)

class MLPHathiResource(resources.ModelResource):

    class Meta:
        model = MLPHathi

class MLPHathiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MLPHathiResource
    list_display = ('hathi_id', 'shorttitle')
    search_fields = ('hathi_id', 'shorttitle', 'prize', 'author', 'person_id', 'inferreddate', 'imprintdate', 'oclc', 'full_name', 'given_name', 'last_name', 'gender')

admin.site.register(MLPHathi, MLPHathiAdmin)

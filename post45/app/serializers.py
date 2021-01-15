from .models import Record, ProgramEraRecord, ProgramEraPeople, ProgramEraGraduations
from rest_framework import serializers


class RecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Record
        fields = ['docid', 'oldauthor', 'author', 'authordate', 'inferreddate', 'latestcomp', 'datetype', 'startdate', 'enddate', 'imprint', 'imprintdate', 'contents', 'genres', 'subjects', 'geographics', 'locnum', 'oclc', 'place', 'recordid', 'enumcron', 'volnum', 'title', 'parttitle', 'shorttitle', 'instances', 'juvenileprob', 'nonficprob']

class ProgramEraRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramEraRecord
        fields = ['docid', 'authors', 'title', 'imprint', 'date', 'place', 'subjects', 'geographics', 'genres', 'classifications', 'locnum', 'oclc', 'isbn']

class ProgramEraPeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramEraPeople
        fields = ['person_id', 'full_name', 'given_name', 'middle_name', 'family_name', 'pen_name', 'gender', 'country']

class ProgramEraGraduationsSerializer(serializers.HyperlinkedModelSerializer):
    #TODO: add advisor_id and graduate_id to the fields and configure their lookup fields properly

    class Meta:
        model = ProgramEraGraduations
        fields = ['record_id', 'graduate_name', 'institution', 'advisor_name', 'year', 'program', 'degree', 'thesis_title', 'genre']

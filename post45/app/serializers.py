from .models import Record, ProgramEraRecord
from rest_framework import serializers


class RecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Record
        fields = ['docid', 'oldauthor', 'author', 'authordate', 'inferreddate', 'latestcomp', 'datetype', 'startdate', 'enddate', 'imprint', 'imprintdate', 'contents', 'genres', 'subjects', 'geographics', 'locnum', 'oclc', 'place', 'recordid', 'enumcron', 'volnum', 'title', 'parttitle', 'shorttitle', 'instances', 'juvenileprob', 'nonficprob']

class ProgramEraRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramEraRecord
        fields = ['docid', 'authors', 'title', 'imprint', 'date', 'place', 'subjects', 'geographics', 'genres', 'classifications', 'locnum', 'oclc', 'isbn']
        

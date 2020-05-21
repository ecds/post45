from .models import Record
from rest_framework import serializers


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    #htrc = serializers.HyperlinkedIdentityField(view_name='htrc-download')

    class Meta:
        model = Record
        fields = ['docid', 'oldauthor', 'author', 'authordate', 'inferreddate', 'latestcomp', 'datetype', 'startdate', 'enddate', 'imprint', 'imprintdate', 'contents', 'genres', 'subjects', 'geographics', 'locnum', 'oclc', 'place', 'recordid', 'enumcron', 'volnum', 'title', 'parttitle', 'shorttitle', 'instances', 'juvenileprob', 'nonficprob']

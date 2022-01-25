from .models import Record, ProgramEraRecord, ProgramEraPeople, ProgramEraGraduations, MasterPrizeRecord, NYTFull, NYTTitle, NYTHathi
from rest_framework import serializers


class RecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Record
        fields = ['docid', 'oldauthor', 'author', 'authordate', 'inferreddate', 'latestcomp', 'datetype', 'startdate', 'enddate', 'imprint', 'imprintdate', 'contents', 'genres', 'subjects', 'geographics', 'locnum', 'oclc', 'place', 'recordid', 'enumcron', 'volnum', 'title', 'parttitle', 'shorttitle', 'instances', 'juvenileprob', 'nonficprob']

class ProgramEraRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramEraRecord
        fields = ['id', 'htid', 'person_id', 'author1_normalized', 'author1', 'author2', 'author3', 'author4', 'title', 'imprint', 'date', 'place', 'subjects', 'geographics', 'lccn', 'oclc', 'isbn']

class ProgramEraPeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProgramEraPeople
        fields = ['person_id', 'full_name', 'given_name', 'middle_name', 'family_name', 'pen_name', 'gender', 'country']

class ProgramEraGraduationsSerializer(serializers.HyperlinkedModelSerializer):
    #TODO: add advisor_id and graduate_id to the fields and configure their lookup fields properly

    class Meta:
        model = ProgramEraGraduations
        fields = ['record_id', 'graduate_name', 'graduate_id', 'institution', 'advisor_name', 'advisor_id', 'year', 'program', 'degree', 'thesis_title', 'genre']


class MasterPrizeRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MasterPrizeRecord
        fields = ['name', 'firstname', 'lastname', 'role', 'prize', 'year', 'genre', 'type', 'amount', 'gender', 'race', 'POCnetwork1', 'POCnetwork2', 'USNWRrank', 'rank', 'ivyflag', 'top50percent', 'harvardflag', 'typeofhighered', 'ba', 'ba2', 'mastersorabove', 'ma', 'ma2', 'mfaflag', 'mfa', 'mfa2', 'phd', 'phd2', 'law', 'med', 'bigfive', 'prizebooktitle', 'careerbooktitle1', 'prizebooktitle2']

class NYTFullSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NYTFull
        fields = ['year', 'week', 'rank', 'title_id', 'title', 'author']

class NYTTitleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NYTTitle
        fields = ['id', 'title', 'author', 'year', 'total_weeks', 'first_week', 'debut_rank', 'best_rank']

class NYTHathiSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NYTHathi
        fields = ['htid', 'title_id', 'title', 'author', 'year', 'first_week', 'debut_rank', 'best_rank']

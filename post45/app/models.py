from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Record(models.Model):
    docid = models.CharField(max_length=255, blank=True, null=True)
    oldauthor = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    authordate = models.CharField(max_length=255, blank=True, null=True)
    inferreddate = models.PositiveIntegerField(blank=True, null=True)
    latestcomp = models.PositiveIntegerField(blank=True, null=True)
    datetype = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.CharField(max_length=255, blank=True, null=True)
    enddate = models.CharField(max_length=255, blank=True, null=True)
    imprint = models.TextField(blank=True, null=True)
    imprintdate = models.CharField(max_length=255, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    genres = models.TextField(max_length=255, blank=True, null=True)
    subjects = models.TextField(blank=True, null=True)
    geographics = models.CharField(max_length=255, blank=True, null=True)
    locnum = models.CharField(max_length=255, blank=True, null=True)
    oclc = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    recordid = models.PositiveIntegerField(blank=True, null=True)
    enumcron = models.CharField(max_length=255, blank=True, null=True)
    volnum = models.PositiveIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    parttitle = models.TextField(blank=True, null=True)
    shorttitle = models.TextField(blank=True, null=True)
    instances = models.PositiveIntegerField(blank=True, null=True)
    juvenileprob = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True, null=True)
    nonficprob = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], blank=True, null=True)

    def __str__(self):
        return self.docid

class ProgramEraRecord(models.Model):
    docid = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    imprint = models.TextField(blank=True, null=True)
    date = models.PositiveIntegerField(blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    subjects = models.TextField(blank=True, null=True)
    geographics = models.CharField(max_length=255, blank=True, null=True)
    genres = models.TextField(max_length=255, blank=True, null=True)
    classifications = models.TextField(max_length=255, blank=True, null=True)
    locnum = models.CharField(max_length=255, blank=True, null=True)
    oclc = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.docid


class ProgramEraPeople(models.Model):
    person_id = models.PositiveIntegerField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    given_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name	= models.CharField(max_length=255, blank=True, null=True)
    family_name	= models.CharField(max_length=255, blank=True, null=True)
    pen_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.person_id


class ProgramEraGraduations(models.Model):
    record_id = models.PositiveIntegerField(primary_key=True)
    graduate_name = models.CharField(max_length=255, blank=True, null=True)
    graduate_id = models.ForeignKey('ProgramEraPeople', blank=True, null=True, on_delete=models.CASCADE, related_name='graduate_id')
    institution = models.CharField(max_length=255, blank=True, null=True)
    advisor_name = models.CharField(max_length=255, blank=True, null=True)
    advisor_id = models.ForeignKey('ProgramEraPeople', blank=True, null=True, on_delete=models.CASCADE, related_name='advisor_id')
    year = models.PositiveIntegerField(blank=True, null=True)
    program = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    thesis_title = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.record_id

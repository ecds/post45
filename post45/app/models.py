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
    htid = models.CharField(max_length=255, blank=True, null=True)
    person_id = models.CharField(max_length=255, blank=True, null=True)
    author1_normalized = models.TextField(blank=True, null=True)
    author1 = models.TextField(blank=True, null=True)
    author2 = models.TextField(blank=True, null=True)
    author3 = models.TextField(blank=True, null=True)
    author4 = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    imprint = models.TextField(blank=True, null=True)
    date = models.PositiveIntegerField(blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    subjects = models.TextField(blank=True, null=True)
    geographics = models.TextField(max_length=255, blank=True, null=True)
    genres = models.TextField(max_length=255, blank=True, null=True)
    classifications = models.TextField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    oclc = models.CharField(max_length=255, blank=True, null=True)
    lccn = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class ProgramEraPeople(models.Model):
    person_id = models.CharField(primary_key=True, max_length=255)
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
    record_id = models.CharField(primary_key=True, max_length=255)
    graduate_name = models.CharField(max_length=255, blank=True, null=True)
    graduate_id = models.CharField(max_length=255, blank=True, null=True)
    institution = models.CharField(max_length=255, blank=True, null=True)
    advisor_name = models.CharField(max_length=255, blank=True, null=True)
    advisor_id = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    program = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    thesis_title = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.record_id


class NYTFull(models.Model):
    year = models.PositiveIntegerField(blank=True, null=True)
    week = models.CharField(max_length=255, blank=True, null=True)
    rank = models.PositiveIntegerField(blank=True, null=True)
    title_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title_id


class NYTTitle(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    total_weeks = models.PositiveIntegerField(blank=True, null=True)
    first_week = models.CharField(max_length=255, blank=True, null=True)
    debut_rank = models.PositiveIntegerField(blank=True, null=True)
    best_rank = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.id

class NYTHathi(models.Model):
    htid = models.CharField(max_length=255, blank=True, null=True)
    title_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    first_week = models.CharField(max_length=255, blank=True, null=True)
    debut_rank = models.PositiveIntegerField(blank=True, null=True)
    best_rank = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.htid

class MLPWinners(models.Model):
    person_id = models.PositiveIntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    given_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    elite_institution = models.CharField(max_length=255, blank=True, null=True)
    graduate_degree = models.CharField(max_length=255, blank=True, null=True)
    mfa_degree = models.CharField(max_length=255, blank=True, null=True)
    iowa_mfa_person_id = models.CharField(max_length=255, blank=True, null=True)
    stegner = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    prize_institution = models.CharField(max_length=255, blank=True, null=True)
    prize_name = models.CharField(max_length=255, blank=True, null=True)
    prize_year = models.PositiveIntegerField(blank=True, null=True)
    prize_genre = models.CharField(max_length=255, blank=True, null=True)
    prize_type = models.CharField(max_length=255, blank=True, null=True)
    prize_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    title_of_winning_book = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name

class MLPHathi(models.Model):
    hathi_id = models.CharField(max_length=255, blank=True, null=True)
    shorttitle = models.CharField(max_length=255, blank=True, null=True)
    prize = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    person_id = models.PositiveIntegerField(blank=True, null=True)
    inferreddate = models.CharField(max_length=255, blank=True, null=True)
    imprintdate = models.CharField(max_length=255, blank=True, null=True)
    oclc = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    given_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.hathi_id

'''
name	firstname	lastname	role	prize	year	genre	type	amount	gender	race	POCnetwork1	POCnetwork2	USNWRrank		ivyflag	top50%	harvardflag	typeofhighered	ba	ba2	mastersorabove	ma	ma2	mfaflag	mfa	mfa2	phd	phd2	law	med	bigfive	prizebooktitle	careerbooktitle1		prizebooktitle2
'''
class MasterPrizeRecord(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    prize = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    race = models.CharField(max_length=255, blank=True, null=True)
    POCnetwork1 = models.CharField(max_length=255, blank=True, null=True)
    POCnetwork2 = models.CharField(max_length=255, blank=True, null=True)
    USNWRrank = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    ivyflag = models.CharField(max_length=255, blank=True, null=True)
    top50percent = models.CharField(max_length=255, blank=True, null=True)
    harvardflag = models.CharField(max_length=255, blank=True, null=True)
    typeofhighered = models.CharField(max_length=255, blank=True, null=True)
    ba = models.CharField(max_length=255, blank=True, null=True)
    ba2 = models.CharField(max_length=255, blank=True, null=True)
    mastersorabove = models.CharField(max_length=255, blank=True, null=True)
    ma = models.CharField(max_length=255, blank=True, null=True)
    ma2 = models.CharField(max_length=255, blank=True, null=True)
    mfaflag = models.CharField(max_length=255, blank=True, null=True)
    mfa = models.CharField(max_length=255, blank=True, null=True)
    mfa2 = models.CharField(max_length=255, blank=True, null=True)
    phd = models.CharField(max_length=255, blank=True, null=True)
    phd2 = models.CharField(max_length=255, blank=True, null=True)
    law = models.CharField(max_length=255, blank=True, null=True)
    med = models.CharField(max_length=255, blank=True, null=True)
    bigfive = models.CharField(max_length=255, blank=True, null=True)
    prizebooktitle = models.CharField(max_length=255, blank=True, null=True)
    careerbooktitle1 = models.CharField(max_length=255, blank=True, null=True)
    prizebooktitle2 = models.CharField(max_length=255, blank=True, null=True)

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import PositiveBigIntegerField
from django.utils import timezone
# Create your models here.


class Applicant(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)


class Education(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    institute = models.CharField(max_length=100)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField(null=True)


class Recruiter(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    bio = models.CharField(max_length=1500)


class Job(models.Model):
    title = models.CharField(max_length=30)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    max_no_of_applications = models.IntegerField()
    max_no_of_positions = models.IntegerField()
    date_of_posting = models.DateTimeField(default=timezone.localtime())
    deadline = models.DateTimeField()
    job_type_choices = [
        ('FT', "Full-Time"),
        ('PT', "Part-TIme"),
        ('WH', "Work from Home")
    ]
    type = models.CharField(
        max_length=2, choices=job_type_choices, default="FT")
    duration = models.PositiveIntegerField(default=0)
    salary = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)


class Language(models.Model):
    name = models.CharField(max_length=20)


class Required(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Has_skill(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=CASCADE)


class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    sop = models.CharField(max_length=1500)
    status_choices = [
        ('AP', 'Applied'),
        ('SH', 'Shortlisted'),
        ('AC', 'Accepted'),
        ('RE', 'Rejected')
    ]
    status = models.CharField(choices=status_choices,
                              default="AP", max_length=2)

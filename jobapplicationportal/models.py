from django.db import models


class JobApplication(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    relevant_experience = models.BooleanField()


class JobReferral(JobApplication):
    referrer_name = models.CharField(max_length=50)
    referrer_email = models.EmailField(max_length=50)

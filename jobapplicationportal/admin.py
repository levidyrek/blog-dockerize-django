from django.contrib import admin

from . import models

admin.site.register(models.JobApplication)
admin.site.register(models.JobReferral)

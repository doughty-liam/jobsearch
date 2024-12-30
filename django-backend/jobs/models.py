from django.db import models

class Job(models.Model):

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=10000)
    date_added = models.DateField()
    shortlisted = models.BooleanField(default=False)
    applied = models.BooleanField(default=False)
    link = models.CharField(default="", max_length=200)

    def __str__(self):
        return str(self.title)+" | "+str(self.location)


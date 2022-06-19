from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from jsonfield import JSONField
from datetime import datetime

class company_model(models.Model):

    company_name = models.CharField(max_length = 50,primary_key=True )
    complaint_email =  models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    twitter = models.CharField(max_length=200)
    number_complaints = models.IntegerField(null=True)
    number_resolutions = models.IntegerField(null=True)
    def __str__(self):
        """
        this makes the name of the item in the database match the title
        """
        return f"{self.company_name}"    

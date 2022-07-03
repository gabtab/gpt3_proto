from django.db import models

from django.contrib.auth.models import User

# Create your models here.
from jsonfield import JSONField
from datetime import datetime


class question(models.Model):
    """
    using the hard coded lists in the below to be selected as a 
    """
    details = models.CharField(max_length = 4000)
    outcome = models.CharField(max_length = 1000)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    amend_date = models.DateField(auto_now = True)
    amend_time = models.TimeField(auto_now = True)
    summary_trans = models.CharField(max_length = 1000)


from django.db import models
from django.conf import settings 
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amend_date = models.DateField(auto_now = True)
    amend_time = models.TimeField(auto_now = True)
    model_output_text = models.CharField(max_length = 1000, blank=True, null=True)
    model_finish_reason = models.CharField(max_length = 100, blank=True, null=True)
    model_log_probs = models.CharField(max_length = 100, blank=True, null=True)
    model_index = models.CharField(max_length = 100, blank=True, null=True)
    model_created = models.CharField(max_length = 100, blank=True, null=True)
    model_id = models.CharField(max_length = 100, blank=True, null=True)
    model_name = models.CharField(max_length = 20, blank=True, null=True)
    model_object = models.CharField(max_length = 20, blank=True, null=True)
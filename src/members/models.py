from django.db import models
from company.models import company_model
from django.contrib.auth.models import User

# Create your models here.
from jsonfield import JSONField
from datetime import datetime

class complaint(models.Model):
    """
    using the hard coded lists in the below to be selected as a 
    """
    goods_choice = [('CG','Consumer Goods'),('ED','Education'),
                    ('EAW','Energy and Water'),('FS','Financial Services'),
                    ('GEN','General Consumer Services'),('HEL','Health'),
                    ('LES','Leisure Services'),('POE','Postal and Electronic Services'),
                    ('TRN','Transport Services'),('OTH', 'Other')
                    ]
    rights_choice = [('TRUTHFUL_AD','Truthful Advertising'),('FAULTY_GDS','Faulty Goods/Replacement'),
                    ('CNTRCT','Unfair Contract'),('RETURNS','Return of Goods within 14 Days'),
                    ('EQUAL_ACCESS','Fair Access to Goods and Services')
                    ]
    class Meta:
        unique_together = (('title','user_name'),)
    title = models.CharField(max_length = 30)
    company_name = models.ForeignKey(company_model,on_delete=models.CASCADE, null = False)
    occurence_date = models.DateField(default=datetime.now)
    good_or_service = models.CharField(max_length = 3,choices = goods_choice, null = True)
    rights_breached = models.CharField(max_length = 12,choices = rights_choice, null = True)
    details = models.CharField(max_length = 4000)
    outcome = models.CharField(max_length = 250)
    contacted_company = models.CharField(default= 'N', max_length = 1, choices = [('Y','Yes'),('N','No')])
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    amend_date = models.DateField(auto_now = True)
    amend_time = models.TimeField(auto_now = True)
    topic_data = models.CharField(max_length = 500)
    sentiment = models.CharField(max_length = 100)
    summary_trans = models.CharField(max_length = 1000)
    def __str__(self):
        """
        this makes the name of the item in the database match the title
        """
        return f"{self.title}"



class question(models.Model):
    """
    using the hard coded lists in the below to be selected as a 
    """
    goods_choice = [('CG','Consumer Goods'),('ED','Education'),
                    ('EAW','Energy and Water'),('FS','Financial Services'),
                    ('GEN','General Consumer Services'),('HEL','Health'),
                    ('LES','Leisure Services'),('POE','Postal and Electronic Services'),
                    ('TRN','Transport Services'),('OTH', 'Other')
                    ]
    rights_choice = [('TRUTHFUL_AD','Truthful Advertising'),('FAULTY_GDS','Faulty Goods/Replacement'),
                    ('CNTRCT','Unfair Contract'),('RETURNS','Return of Goods within 14 Days'),
                    ('EQUAL_ACCESS','Fair Access to Goods and Services')
                    ]
    class Meta:
        unique_together = (('title','user_name'),)
    title = models.CharField(max_length = 30)
    company_name = models.ForeignKey(company_model,on_delete=models.CASCADE, null = False)
    occurence_date = models.DateField(default=datetime.now)
    good_or_service = models.CharField(max_length = 3,choices = goods_choice, null = True)
    rights_breached = models.CharField(max_length = 12,choices = rights_choice, null = True)
    details = models.CharField(max_length = 4000)
    outcome = models.CharField(max_length = 250)
    contacted_company = models.CharField(default= 'N', max_length = 1, choices = [('Y','Yes'),('N','No')])
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    amend_date = models.DateField(auto_now = True)
    amend_time = models.TimeField(auto_now = True)
    topic_data = models.CharField(max_length = 500)
    sentiment = models.CharField(max_length = 100)
    summary_trans = models.CharField(max_length = 1000)
    def __str__(self):
        """
        this makes the name of the item in the database match the title
        """
        return f"{self.title}"
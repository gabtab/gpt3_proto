from django.db import models

# Create your models here.

class agent(models.Model):
    """
    a class for an agent 
    this needs to be worked on for uniqueness as well as creating all of the
    criteria for an agent
    """
    user_name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length = 30, null =True, blank = True)
    amend_date = models.DateField(auto_now = True)
    amend_time = models.TimeField(auto_now = True)
    def __str__(self):
        """
        this makes the name of the item in the database match the user_name
        """
        return f"{self.user_name}"
    


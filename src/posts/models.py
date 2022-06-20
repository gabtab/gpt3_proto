from django.db import models

# Create your models here.
class Post(models.Model):
    """
    a class for a post this will probably be used for posting a message to twitter
    or other social media. needs to get all of the parameters and may need
    to be stored in kafka topic eventually
    """
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=500)
    agent = models.CharField(max_length=50)
    amend_date = models.DateField(auto_now = True)
    amend_time = models.TimeField(auto_now = True)
    def __str__(self):
        """
        returns the title of the post in the db or when called
        """
        return f"{self.title}"
    


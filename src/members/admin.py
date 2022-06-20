from django.contrib import admin
from .models import complaint

# Register your models here.

admin.site.register(complaint) 


def delete_everything(self):
    complaint.objects.all().delete()
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from members.models import question



def home(request):
    """
    this is a test view that is created to show how you can use variables in this
    and push them into the template. see template, welcome.html and url sheet in 
    webagent app
    """
    return render(request, "home.html",
                  {"current_time": datetime.now(),
                   
                   })

def index(request):
    """
    this is a test view that is created to show how you can use variables in this
    and push them into the template. see template, welcome.html and url sheet in 
    webagent app
    """
    return render(request, "index.html",
                  {"current_time": datetime.now(),
                   
                   })



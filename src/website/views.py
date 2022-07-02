from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from posts.models import Post
from agent.models import agent
from django.contrib.auth.models import User
from members.models import complaint

# Create your views here.
def welcome(request):
    """
    this is a test view that is created to show how you can use variables in this
    and push them into the template. see template, welcome.html and url sheet in 
    webagent app
    """
    return render(request, "welcome.html",
                  {"current_time": datetime.now(),
                   "Posts": Post.objects.all(),
                   "num_posts": Post.objects.count(),
                   "Agents": agent.objects.all(),
                   "num_agents": agent.objects.count(),
                   #"num_clients": client.objects.count(),
                   #"clients": client.objects.all(),
                   "num_complaints": complaint.objects.count(),
                   "num_members": User.objects.count(),
                   })


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



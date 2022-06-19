from django.shortcuts import render, redirect
from .forms import agent_form
# Create your views here.

def agent_input(request):
    if request.method == "POST":
        form = agent_form(request.POST)
        if form.is_valid():
           form.save()
           return redirect("/")
    else:
        form= agent_form()
    return render(request, "agent_page.html", {"form":form})
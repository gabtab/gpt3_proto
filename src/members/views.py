from .forms import NewUserForm, client_question, answer
from .models import question
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="client_page.html", context={"form":form})




@login_required(login_url="login_user")
def question_input(request):
    """
    The question webpage view. this uses
    a form for completing the question data(must be logged in)
    """
 #   submitted = False
    if request.method == "POST":
        form = client_question(request.POST,initial={'user_id': request.user.id})
        answer_output = form.instance.model_output_text
        if form.is_valid():
            form.save()
            answer_output = form.instance.model_output_text
            form = answer(initial={'user_name': request.user})
            form.instance.model_output_text = answer_output
            return render(request, "answer.html", {"form":form, 'answer':answer_output})
            
            
    else:
        form = client_question()
    return render(request, "client_question.html", {"form":form})





def login_user(request):
    """
    a view that checks for username and password in the html, pulls it

    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
     
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            messages.success(request, ('You are now logged in as ' + str(user)))
            return redirect('/')

        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an error logging in, please try again'))
            return redirect('login_user')
    
    
    else:
        return render(request, 'login.html', {})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")




"""

@login_required(login_url="login_user")
def answer(request):

 #   submitted = False
    if request.method == "GET":
        form = answer(initial={'user_name': request.user})
    return render(request, "answer.html")
"""
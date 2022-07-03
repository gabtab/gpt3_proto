from .forms import NewUserForm, client_question
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
        form = client_question(request.POST)
        if form.is_valid():
            form.save()
            
            
            """ next few lines were used to get the sentiment and topics into webpage
            question_topic = question.objects.filter(title = form['title'].value(), \
                                                      user_name = request.user).values('topic_data','sentiment')
             
            test1 = question_topic[0]['topic_data']
            test2 = question_topic[0]['sentiment']
            question_topic =  str(test1).strip('[]')
            topic_message = "The key issues identified from you question are " + str(question_topic) + " \r\n" + \
            "The sentiment is " + str(test2)
             probably no need for the above few lines once upskilles   """ 
        
            return redirect("/")
            
            
    else:
        form = client_question(initial={'user_name': request.user})
        topic_message = ''
    return render(request, "client_question.html", {"form":form, "topic_message": topic_message})





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
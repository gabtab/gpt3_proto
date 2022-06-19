from .forms import NewUserForm, client_complaint
from .models import complaint
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
def complaint_input(request):
    """
    The complaint webpage view. this uses
    a form for completing the complaint data(must be logged in)
    """
    #submitted = False
    if request.method == "POST":
        form = client_complaint(request.POST)
        if form.is_valid():
            form.save()
            
            
            """ next few lines were used to get the sentiment and topics into webpage
            complaint_topic = complaint.objects.filter(title = form['title'].value(), \
                                                      user_name = request.user).values('topic_data','sentiment')
             
            test1 = complaint_topic[0]['topic_data']
            test2 = complaint_topic[0]['sentiment']
            complaint_topic =  str(test1).strip('[]')
            topic_message = "The key issues identified from you complaint are " + str(complaint_topic) + " \r\n" + \
            "The sentiment is " + str(test2)
             probably no need for the above few lines once upskilles   """ 
        
            return redirect("/")
            
            
    else:
        form = client_complaint(initial={'user_name': request.user})
        topic_message = ''
    return render(request, "client_complaint.html", {"form":form, "topic_message": topic_message})





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
        return render(request, 'authenticate/login.html', {})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")
from django.forms import ModelForm
from django import forms
from .models import question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from analytics_hub.AI_models.summarise_complaint import gpt3_summary
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


myapi_keys = {}
with open("/etc/django/openai.txt") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        myapi_keys[name.strip()] = var.strip()


class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length = 30)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()       
        return user

        
class client_question(ModelForm):
    class Meta:
            model = question
            widgets = {'details':forms.Textarea({'rows': '8'})
                   }
            
            fields = ['details','user']
        

    def save(self):
        """
        the topic modelling etc needs to happen after the page has been re-directed
        in the view and before the database has been updated. therefore we
        can use whats in the form to populate the db while the user has been 
        re-directed back to home
        """
        gpt3_output = gpt3_summary(self.cleaned_data['details'],myapi_keys)
        
        
        inputted_question = super(client_question, self).save(commit=False)
        inputted_question.user_name = self.cleaned_data.get('username')
        inputted_question.model_output_text = gpt3_output.choices[0]['text']
        inputted_question.model_finish_reason = gpt3_output.choices[0]['finish_reason']
        inputted_question.model_log_probs = gpt3_output.choices[0]['logprobs']
        inputted_question.model_index = gpt3_output.choices[0]['index']
        inputted_question.model_created = gpt3_output.created
        inputted_question.model_id = gpt3_output.id
        inputted_question.model_name = gpt3_output.model
        inputted_question.model_object = gpt3_output.object
        inputted_question.save() 
        #self.send_mail(inputted_complaint.summary_trans)
        return inputted_question

class answer(ModelForm):
    class Meta:
            model = question
            widgets = {'model_output_text':forms.Textarea({'rows': '8'})
                   }
            
            fields = ['model_output_text']
        

from . import views
from django.urls import path, include, re_path



urlpatterns = [
   path('login_user', views.login_user, name = 'login_user'),
   re_path(r'^client_input',views.register_request, name='client_input_tab' ),
   #re_path(r'^complaint_input',views.complaint_input, name='complaint_input_tab' ),
   re_path(r'^question_input',views.question_input, name='question_input_tab' ),
]

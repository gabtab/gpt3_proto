# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import agent

class agent_form(ModelForm):
    class Meta:
        model = agent
        exclude = ['amend_date','amend_time']
from django.shortcuts import render
from .models import Survey
from .forms import SurveyForm
from django.views.generic import (CreateView)
from . import forms
# Create your views here.

def index(request):
    return render(request, 'appsurvey/index.html')

def formname(request):
    form = forms.SurveyForm()

    if request.method == 'POST':
        form = forms.SurveyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'appsurvey/thankyou.html')
        else:
            print("ERROR FORM INVALID")

    return render(request, 'appsurvey/about.html', {'form':form})

def thankyou(request):
    return render(request, 'appsurvey/thankyou.html')

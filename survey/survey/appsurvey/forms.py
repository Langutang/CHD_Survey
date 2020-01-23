from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):

    class Meta():
        model = Survey
        fields = ('email', 'restriction', 'jeans', 'dressshort', 'attend')
        labels = {
        'email':'Please enter your email (optional)',
        'restriction':'Do you think the current dress code requirements are:',
        'jeans':'Do you think the dress code should be relaxed to allow dress blue jeans/denim?',
        'dressshort':'Do you think the dress code should be relaxed to allow dress shorts?',
        'attend':'Do you think that you are likely to attend more race days if the dress code was relaxed to allow dress blue jeans/denim and dress shorts?'
        }

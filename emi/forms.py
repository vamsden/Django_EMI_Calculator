from django import forms 
from django.forms import ModelForm

class emiforms(forms.ModelForm):
	loanAmount = forms.IntegerField()
	intrate = forms.IntegerField()
	period = forms.IntegerField()


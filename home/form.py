from django import forms
from .models import *
#forms.Form 개별적
#forms.ModelForm 전체적
class Createsignup(forms.ModelForm):
    myid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'아이디 적으셈'}))
    pw=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Member
        fields=['myid','pw','name']
class Createlogin(forms.ModelForm):
    myid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'아이디 적으셈'}))
    pw=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Member
        fields=['myid','pw']

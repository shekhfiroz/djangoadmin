from django import forms
#writing a contactus form of a website

class ContactusForm(forms.Form):
    fname=forms.CharField()
    lname=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(required=False)
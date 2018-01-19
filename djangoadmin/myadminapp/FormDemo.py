from django import forms
#writing a contactus form of a website

class ContactusForm(forms.Form):

    def formcontent(self):
        fname=forms.CharField()
        lname=forms.CharField()
        email=forms.EmailField()
        message=forms.CharField(required=False)

contactusform=ContactusForm()
contactusform.formcontent()

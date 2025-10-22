from django import forms
from .models import Contact
#class ContactForm(forms.Form):
#    name=forms.CharField(max_length=50,label='yourname')
#    email=forms.EmailField(label='email_id')
#    message=forms.CharField(label='enter your message')
#    firstname=forms.CharField(label='firstname')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=['title','uploaded_file']
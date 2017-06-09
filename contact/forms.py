import datetime

from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['timestamp']

        # overriding the function for checking validation of email
        def clean_email(self):
            print("Hello")
            email = self.cleaned_data['email']
            if not "gmail" in email:
                raise forms.ValidationError("Please use a valid email address")
            return email
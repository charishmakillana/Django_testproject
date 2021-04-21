from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from testapp.models import *
from django.core.validators import RegexValidator

def phone_number_validator():
    return RegexValidator(regex=r'^\+?1?\d{9,15}$',
                          message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class UserForm(forms.Form):

    name = forms.CharField()
    URL = forms.URLField()
    phone_number = forms.CharField(
        label='Enter Phone number', max_length=15, min_length=10, validators=[phone_number_validator()]
    )

    def clean(self):
        data = self.cleaned_data['name']

        if len(data) < 5:
            raise ValidationError('Minimum 5 characters required for name field')

        return self.cleaned_data





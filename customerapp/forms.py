from django import forms
from .models import  Customer,Account
from django.contrib.auth.models import User


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','email','address','image')

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('customer','balance',)
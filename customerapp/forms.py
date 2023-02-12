from django import forms
from .models import  Customer,Account,Cards
from django.contrib.auth.models import User


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','email','address','image','account_number')

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('customer','balance',)
class CardForm(forms.ModelForm):
    class Meta:
        model=Cards
        fields=('account','card_number',)        
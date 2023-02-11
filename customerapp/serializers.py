from rest_framework import serializers
from .models import Customer, Account,Cards

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Mete:
        model =Account
        fields= '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        models=Cards
        fields='__all__'             

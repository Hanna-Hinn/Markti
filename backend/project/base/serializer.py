from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'        
        
class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = '__all__'     

class APIMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIMethods
        fields = '__all__'   


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
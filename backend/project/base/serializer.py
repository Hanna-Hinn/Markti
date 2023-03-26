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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class APIMethodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = APIMethods
        fields = '__all__'


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = '__all__'

    methods = serializers.SerializerMethodField()

    def get_methods(self, obj):
        model2_queryset = APIMethods.objects.filter(mainAPI=obj)
        serializer = APIMethodsSerializer(model2_queryset, many=True)
        return serializer.data


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class AliExpressProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    evaluate_rate = serializers.CharField(max_length=100)
    first_level_category_name = serializers.CharField(max_length=100)
    original_price = serializers.CharField(max_length=100)
    original_price_currency = serializers.CharField(max_length=100)
    product_detail_url = serializers.CharField(max_length=300)
    product_main_image_url = serializers.CharField(max_length=300)
    product_title = serializers.CharField(max_length=100)
    promotion_link = serializers.CharField(max_length=300)
    second_level_category_name = serializers.CharField(max_length=100)
    
class AliExpressListSerializer(serializers.ListSerializer):
    child = AliExpressProductSerializer()


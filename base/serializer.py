from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

"""
    This class is responsible for converting objects into data types understandable by javascript and front-end frameworks. 
    Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
    
"""

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'


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

    def delete(self, validated_data):
        instance = self.instance
        instance.delete()


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def delete(self, validated_data):
        instance = self.instance
        instance.delete()


class AliExpressProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    evaluate_rate = serializers.CharField(max_length=200, required=False)
    first_level_category_name = serializers.CharField(max_length=100)
    original_price = serializers.CharField(max_length=100)
    product_detail_url = serializers.CharField(max_length=300)
    product_main_image_url = serializers.CharField(max_length=300)
    product_title = serializers.CharField(max_length=100)
    promotion_link = serializers.CharField(max_length=300)

class IkeaProductSerializer(serializers.Serializer):
    id= serializers.CharField(max_length=50)
    #current_price = serializers.SerializerMethodField()
    image = serializers.CharField(max_length=200)
    url= serializers.CharField(max_length=200)

class EbayProductSerializer(serializers.Serializer):
    itemId = serializers.IntegerField()
    title = serializers.CharField()
    categoryName = serializers.SerializerMethodField()
    galleryURL = serializers.CharField(max_length=200)
    viewItemURL = serializers.CharField(max_length=200)
    value = serializers.SerializerMethodField()
    sellingState = serializers.SerializerMethodField()
    topRatedListing = serializers.CharField(max_length=100)

    # description = serializers.CharField(max_length=250)

    def get_categoryName(self, obj):
        return obj['primaryCategory']['categoryName']

    def get_value(self, obj):
        return obj['sellingStatus']['currentPrice']['value']

    def get_sellingState(self, obj):
        return obj['sellingStatus']['sellingState']

    def get_watchCount(self, obj):
        return obj['listingInfo']['watchCount']


class AmazonRapidProductSerializer(serializers.Serializer):
    asin = serializers.CharField(max_length=50)
    current_price = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()  # in numbers
    url = serializers.CharField(max_length=200)
    amazonChoice = serializers.CharField(max_length=50)
    bestSeller = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=200)
    thumbnail = serializers.CharField(max_length=200)
   # description = serializers.CharField(max_length=250)

    def get_current_price(self, obj):
        return obj['price']['current_price']

    def get_total_reviews(self, obj):
        return obj['reviews']['total_reviews']

    def get_rating(self, obj):
        return obj['reviews']['rating']


class SheinRapidProductSerializer(serializers.Serializer):
    goods_id= serializers.CharField(max_length=50)
    goods_img = serializers.CharField(max_length=200)
    goods_url_name = serializers.CharField(max_length=100)
    usdAmountWithSymbol = serializers.SerializerMethodField()
    comment_rank_average = serializers.CharField(max_length=50)
    generatedURL = serializers.CharField(max_length=300)





    def get_usdAmountWithSymbol(self, obj):
        return obj['retailPrice']['usdAmountWithSymbol']


class RealTimeProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=50)
    product_title = serializers.CharField(max_length=100)

    product_page_url = serializers.CharField(max_length=200)
   # product_num_reviews = serializers.IntegerField()
    product_photo_url = serializers.SerializerMethodField()
    product_rating = serializers.CharField(max_length=50)

    price_range = serializers.SerializerMethodField()
    # product_description = serializers.CharField(max_length=250)

    def get_product_photo_url(self, obj):
        return obj['product_photos'][0]

    def get_price_range(self, obj):
        return obj['typical_price_range']
# Fadis eddition


class ProductSerializer(serializers.Serializer):
    product_id = serializers.CharField()
    product_title = serializers.CharField()

    product_image = serializers.URLField()
    product_url = serializers.URLField()
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    product_store = serializers.CharField()
    # make sure to add the store image can be found in store images
    product_store_image = serializers.URLField()

    # in frontend, we check if ratiing is char or int EBAY RETURNS IF THE SELLER IS NOT TOP RATED
    product_rating = serializers.CharField()

    product_trusted = serializers.CharField()

    # product_description = serializers.CharField()

    # note for why it is char
   # The eBay API does not provide the rating of an item directly.
   # The "topRatedListing" field or parameter in the eBay API SDK is
   # used to filter or retrieveitems that are eligible for eBay's
   # Top Rated Plus program based on specific criteria such
   # as fast shipping, accurate item descriptions, and excellent customer service.

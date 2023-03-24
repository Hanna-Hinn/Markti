            #Django Imports# 
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files import File
#######################################
          #Rest Framework Imports#
from rest_framework.decorators import api_view
from rest_framework.response import Response

#######################################
            #Python Imports#
import requests
import pandas as pd
from .models import Product
import json
from .secrets import *

#######################################
            #Api Imports#
#AliExpress
from topsdk.client import TopApiClient, TopException
#Ebay
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

#######################################
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/search',
        
        '/api/tickets',
        '/api/tickets/create',
        '/api/tickets/<id>',
        '/api/tickets/<modify>/<id>',
        
        '/api/apis',
        '/api/apis/create',
        '/api/apis/<id>',
        '/api/apis/<modify>/<id>',
    ]
    return Response(routes)

@api_view(['GET'])
def search(request):
    return Response("I am Searching")

@api_view(['POST'])
def createTicket(request):
    return Response("I Create Ticket")


@api_view(['GET'])
def getTickets(request):
    return Response("I Fetch all Tickets")


@api_view(['GET'])
def getTicket(request, pk):
    return Response("I Fetch Ticket with ID = " + str(pk))

@api_view(['POST','PUT','DELETE'])
def modifyTicket(request,modify,pk):
    if request.method == "POST":
        return Response("Modifying " + modify + " ID: " + pk + "Ticket using POST")
    elif request.method == "PUT":
        return Response("Updating " + modify + " ID: " + pk + "Ticket using PUT")
    elif request.method == "DELETE":
        return Response("Deleting " + modify + " ID: " + pk + "Ticket using DELETE")
    else :
        return Response("UnValid Method")
    
@api_view(['GET'])
def getAPIs(request):
    return Response("I Fetch all APIs")

@api_view(['POST'])
def createAPI(request):
    return Response("I Create APIs")

@api_view(['GET'])
def getAPI(request, pk):
    return Response("I Fetch API with ID = " + str(pk))

@api_view(['POST','PUT','DELETE'])
def modifyAPI(request,modify,pk):
    if request.method == "POST":
        return Response("Modifying " + modify + " ID: " + pk + "API using POST")
    elif request.method == "PUT":
        return Response("Updating " + modify + " ID: " + pk + "API using PUT")
    elif request.method == "DELETE":
        return Response("Deleting " + modify + " ID: " + pk + "API using DELETE")
    else :
        return Response("UnValid Method")
    
###############################
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    return Response(products)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    return Response(product)

@api_view(['GET'])
def getProductsByStore(request, store):
    products = Product.objects.filter(Store=store)
    return Response(products)

@api_view(['GET'])
def getProductsByCategory(request, category):
    products = Product.objects.filter(Category=category)
    return Response(products)

@api_view(['GET'])
def getProductsBySubCategory(request, subcategory):
    products = Product.objects.filter(SubCategory=subcategory)
    return Response(products)

@api_view(['GET'])
def getProductsByBrand(request, brand):
    products = Product.objects.filter(Brand=brand)
    return Response(products)

@api_view(['GET'])
def getProductsByPrice(request, price):
    products = Product.objects.filter(Price=price)
    return Response(products)

@api_view(['GET'])
def getProductsByRating(request, rating):
    products = Product.objects.filter(Rating=rating)
    return Response(products)

@api_view(['GET'])
def getProductsByDiscount(request, discount):
    products = Product.objects.filter(Discount=discount)
    return Response(products)

@api_view(['GET'])
def productCount(request):
    productCount = Product.objects.all().count()
    return Response(productCount)

@api_view(['GET'])
def productCountFromStore(request, store):
    productCount = Product.objects.filter(Store=store).count()
    return Response(productCount)

@api_view(['GET'])
def productCountFromCategory(request, category):
    productCount = Product.objects.filter(Category=category).count()
    return Response(productCount)

@api_view(['GET'])
def productCountFromSubCategory(request, subcategory):
    productCount = Product.objects.filter(SubCategory=subcategory).count()
    return Response(productCount)

###############################


###########################
# Function : callApi
# Input : request , keyword(Search String)
# Output : Response (mostly Json)
# Description : This function is used to call the APIs and return the data in Json format
###########################

# pip install ebaysdk
@api_view(['GET'])
def callApi_Ebay(request, keyword):
    
        api = Finding(appid= Ebay_API_KEY , config_file=None)
        api_request = {'keywords': keyword}
        try:
            response = api.execute('findItemsAdvanced', api_request)
            # df = pd.DataFrame() 
            # df['id'] = [item.itemId for item in response.reply.searchResult.item] 
            # df['Name'] = [item.title for item in response.reply.searchResult.item]
            # df['Price(USD)'] = [item.sellingStatus.currentPrice.value for item in response.reply.searchResult.item]
            # df['Category'] = [item.primaryCategory.categoryName for item in response.reply.searchResult.item]
            # df['Rating'] = [item.storeInfo.storeName for item in response.reply.searchResult.item]
            # df['Discount'] = [item.storeInfo.storeName for item in response.reply.searchResult.item]
            # df['Image'] = [item.galleryURL for item in response.reply.searchResult.item]
            # df['URL'] = [item.viewItemURL for item in response.reply.searchResult.item]
            # df['Description'] = [item.title for item in response.reply.searchResult.item]
            return Response(response.json)
        except Exception as e:
            print(e)
            return Response(e)
        
@api_view(['GET'])
def callApi_Rapid_AliExpress(request,keyword):
        try: 
            client = TopApiClient(appkey= AlIEXPRESS_APP_KEY , app_sercet= AlIEXPRESS_API_KEY  ,
                          top_gateway_url='http://api.taobao.com/router/rest', verify_ssl=False)
            
            request_dict = {
            "app_signature": "Marekti",
            "keywords": keyword,
            "page_no": "1",
            "target_currency": "USD",
            "target_language": "en",
            "tracking_id": "Marketi",
            }

            file_param_dict = {}
            response = client.execute("aliexpress.affiliate.product.query",request_dict,file_param_dict)
            # json_obj = json.dumps(response, indent=4)
            products = response.get('resp_result').get('result').get('products')
            json_obj = json.dumps(products, indent=1)
            return Response(json_obj)
        
        except TopException as e:
            print(e)
            return Response("Error")
        
@api_view(['GET'])
def callApi_Rapid_AmazonApi(request,keyword):
        try:
    
            url = "https://amazon-product-reviews-keywords.p.rapidapi.com/product/search"

            querystring = {"keyword":keyword}

            headers = {
                "X-RapidAPI-Key": RAPID_API_KEY,
                "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            return Response(response.json())
        except Exception as e:
            print(e)
            return Response("Error")
        
@api_view(['GET'])
def callApi_Rapid_Shein(request,keyword):
        try:
            url = "https://unofficial-shein-api.p.rapidapi.com/search"

            querystring = {"query": keyword}

            headers = {
                'X-RapidAPI-Key': RAPID_API_KEY,
                'X-RapidAPI-Host': 'unofficial-shein.p.rapidapi.com'
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            return Response(response.json())

        except Exception as e:
            print(e)
            return Response("Error")
        
@api_view(['GET'])
def callApi_Rapid_RealTime(request,keyword):     
    try:
        url = "https://unofficial-shein-api.p.rapidapi.com/search"

        querystring = {"query":keyword}

        headers = {
            'X-RapidAPI-Key': RAPID_API_KEY,
            'X-RapidAPI-Host': 'real-time-product-search.p.rapidapi.com'
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return Response(response.json())
        
    except Exception as e:
        print(e)
        return Response("Error")



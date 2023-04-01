

######################################
                #Python Imports#

import threading as th
import requests
from rest_framework.response import Response

#######################################
                #Data Imports#

from . import secrets 
#######################################
                #Class Imports#
                
from .serializer import *
#######################################
                #Api Imports#

#AliExpress
from topsdk.client import TopApiClient, TopException
#Ebay
from ebaysdk.finding import Connection as Finding
#######################################
                #Variables#

results= [] # this is a list that will store the results from the API calls in the watchDog.py file

results_lock = th.Lock() # this is a lock that will be used to lock the results list used in the watchDog.py file

finished = False # this is a boolean that will be used to tell the dataManager.py file that the watchDog.py file has finished

keyWord ="" # this is a string that will be used to store the keyword that the user has entered

###########################
# Function : callApi
# Input : request , keyword(Search String)
# Output : Response (mostly Json)
# Description :
# ----------------------------
#  This function is used to call the APIs and return the data in Json format
# ----------------------------
###########################

def callApi_Ebay():
    
        api = Finding(appid= secrets.EBAY_API_KEY , config_file=None)
        api_request = {'keywords': keyWord}
        try:
            response = api.execute('findItemsAdvanced', api_request)
            json_response = response.dict()
            products = json_response.get('searchResult').get('item')
            serializer = EbayProductSerializer(products,many=True)
            return serializer.data
        except Exception as e:
            print(e)
            return e
        

def callApi_Rapid_AliExpress(keyword):
        try: 
            client = TopApiClient(appkey= secrets.ALIEXPRESS_APP_KEY , app_sercet= secrets.ALIEXPRESS_API_KEY  ,
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
            products = response.get('resp_result').get('result').get('products')
            serializer = AliExpressProductSerializer(products,many=True)
            return serializer.data
        
        except TopException as e:
            print(e)
            return Response("Error")
        

def callApi_Rapid_AmazonApi(keyword):
        try:
    
            url = "https://amazon23.p.rapidapi.com/product-search"

            querystring = {"query":keyword}

            headers = {
                "X-RapidAPI-Key": secrets.RAPID_API_KEY,
                "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            products = response.json().get('result')
            serializer = AmazonRapidProductSerializer(products,many=True)
            return serializer.data
        except Exception as e:
            return e
        

def callApi_Rapid_SheinAPI(request,keyword):
        try:
            url = "https://unofficial-shein.p.rapidapi.com/products/search"

            querystring = {"keywords":keyword,"language":"en","country":"US","currency":"USD"}

            headers = {
                'X-RapidAPI-Key': secrets.RAPID_API_KEY,
                'X-RapidAPI-Host': 'unofficial-shein.p.rapidapi.com'
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            products = response.json().get('info').get("products")
            serializer = SheinRapidProductSerializer(products,many=True)
            return serializer.data

        except Exception as e:
            return e
        
def callApi_Rapid_RealTime(keyword):     
    try:
        url = "https://real-time-product-search.p.rapidapi.com/search"

        querystring = {"q":keyword,"country":"us","language":"en"}

        headers = {
            'X-RapidAPI-Key': "5d35771659msh1de8eff53abd5afp14756fjsn875eab81aa56",
            'X-RapidAPI-Host': 'real-time-product-search.p.rapidapi.com'
            }

        response = requests.request("GET", url, headers=headers, params=querystring) 
        products = response.json().get('data')
        serializer = RealTimeProductSerializer(products,many=True)
    
        return serializer.data
        
    except Exception as e:
        return e

def callApi_FakeStore():
    response = requests.get('https://fakestoreapi.com/products?limit=5')
    if response.status_code == 200:
        data = response.json()
        #make a list of the product prices
        prices = [product['price'] for product in data]
        return prices
    else:
        print('Error fetching data from API')


############################################################################################################
#Name : API_Dectionary
#Description : 
#              This is a dictionary that contains the name of the API and the function that calls it.
#              This is used in the watchDog.py file to call the API functions.
#              The key is the name of the API and the value is the function that calls it.
#              The function that calls the API is in the views.py file.
###################################################

API_Dectionary = {
        "Rapid_Amazon" :        callApi_Rapid_AmazonApi, 
        "Rapid_AliExpress":     callApi_Rapid_AliExpress, 
        "Ebay":                 callApi_Ebay, 
        "FakeStore":            callApi_FakeStore ,
        "Rapid_Shein":          callApi_Rapid_SheinAPI
        }

############################################################################################################

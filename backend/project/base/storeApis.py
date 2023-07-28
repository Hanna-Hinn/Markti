

######################################
# Python Imports#


import requests
from rest_framework.response import Response

#######################################
# Data Imports#

from . import secrets
#######################################
# Class Imports#

from .serializer import *

#######################################
# Api Imports#

# AliExpress
from topsdk.client import TopApiClient, TopException
# Ebay
from ebaysdk.finding import Connection as Finding
#######################################

###########################
# Function : callApi
# Input : request , keyword(Search String)
# Output : Response (mostly Json)
# Description :
# ----------------------------
#  This function is used to call the APIs and return the data in Json format
# ----------------------------
###########################


def callApi_Ebay(keyword):
    api = Finding(appid= secrets.EBAY_API_KEY, config_file=None)
    api_request = {'keywords': keyword}
    
    try:
        response = api.execute('findItemsAdvanced', api_request)
        json_response = response.dict()
        products = json_response.get('searchResult').get('item')
        
        # check if the response code is 200
        if statusCheck(response):
            return statusCheck(response)
        
        try:
            serializer = EbayProductSerializer(products, many=True)
            return serializer.data 
        except Exception as e:
            print("Error in serializer", e) 
    except ConnectionError as e:
        print("ERROR IN CALL_EBAY FUNCTION IN STORES_API", e)
        




def callApi_Rapid_AliExpress(keyword):
    try:
        client = TopApiClient(appkey=secrets.ALIEXPRESS_APP_KEY, app_sercet=secrets.ALIEXPRESS_API_KEY,
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
        response = client.execute(
            "aliexpress.affiliate.product.query", request_dict, file_param_dict)

        # Check if the response is None
        if response is not None:
            resp_result = response.get('resp_result')
            if resp_result is not None:
                result = resp_result.get('result')
                if result is not None:
                    products = result.get('products', [])
    
                    serializer = AliExpressProductSerializer(products, many=True)
                    return serializer.data

        # If response is None or any required attribute is missing, return an empty list
        return []

    except TopException as e:
        print("test", e)
        # return Response("Error")
   

def callApi_Rapid_AmazonApi(keyword):
    try:

        url = "https://amazon23.p.rapidapi.com/product-search"

        querystring = {"query": keyword}

        headers = {
            "X-RapidAPI-Key": secrets.RAPID_API_KEY,
            "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        products = response.json().get('result')
        serializer = AmazonRapidProductSerializer(products, many=True)
        return serializer.data
    except Exception as e:
        
        return e



def callApi_Rapid_SheinAPI(keyword):
    try:
        url = "https://unofficial-shein.p.rapidapi.com/products/search"

        querystring = {
            "keywords": keyword,
            "language": "en",
            "country": "US",
            "currency": "USD"
        }

        headers = {
            'X-RapidAPI-Key': secrets.RAPID_API_KEY,  # Make sure secrets.RAPID_API_KEY is defined
            'X-RapidAPI-Host': 'unofficial-shein.p.rapidapi.com'
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response_data = response.json()

        # Check if 'info' and 'products' exist in the response data
        info = response_data.get('info')
        if not info or 'products' not in info:
            return []  # Return an empty list if the required data is not present

        products = info.get("products")

        # Generate the URL for each product
        for product in products:
            product['generatedURL'] = "https://us.shein.com/" +str(product['goods_url_name']).replace(" ", "-") + "-p-" + str(product['goods_id']) + ".html"

        
        serializer = SheinRapidProductSerializer(products, many=True)
        return serializer.data

    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)
        return []
    except Exception as e:
        print("Error:", e)
        return []


    except Exception as e:
        return e

def callApi_Rapid_Ikea(keyword):
    try:
        url = "https://ikea.p.rapidapi.com/products/search"

        querystring = {
            "query": keyword,
            "countryCode": 'us',
            "languageCode": 'en'
        }

        headers = {
            'X-RapidAPI-Key': secrets.RAPID_API_KEY,  # Make sure secrets.RAPID_API_KEY is defined
            'X-RapidAPI-Host': 'unofficial-shein.p.rapidapi.com'
        }

        response = requests.get(url, headers=headers, params=querystring)
        
        # Check the status code to see if the API call was successful
        if response.status_code == 200:
            # Process the response here and return the relevant data
            products = response.json()  # Assuming the API returns JSON data
            serializer = IkeaProductSerializer(products, many=True)
            return "response"
        else:
            # If the API call was not successful, you might want to handle the error
            response.raise_for_status()
            return response

    except Exception as e:
        print("Error:", e , "in" , "callApi_Rapid_Ikea")
        return e

def callApi_FakeStore():
    response = requests.get('https://fakestoreapi.com/products?limit=5')
    if response.status_code == 200:
        data = response.json()
        # make a list of the product prices
        prices = [product['price'] for product in data]
        return prices
    else:
        print('Error fetching data from API')


############################################################################################################
# Name : API_Dectionary
# Description :
#              This is a dictionary that contains the name of the API and the function that calls it.
#              This is used in the watchDog.py file to call the API functions.
#              The key is the name of the API and the value is the function that calls it.
#              The function that calls the API is in the views.py file.
###################################################

API_Dectionary = {
    "Amazon":        callApi_Rapid_AmazonApi,
    "AliExpress":     callApi_Rapid_AliExpress,
    "Ebay":           callApi_Ebay,
    "FakeStore":      callApi_FakeStore,
    "Shein":          callApi_Rapid_SheinAPI,
    "Ikea":           callApi_Rapid_Ikea,
}


############################################################################################################

def statusCheck(response):
     print(response.status_code)
     if response.status_code != 200:
            print("Error: " + str(response.status_code))

            return "Error: " + str(response.status_code)
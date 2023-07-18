#######################################
# Python Imports#
import keyword
import requests

#######################################
# Api Imports#
# AliExpress
from topsdk.client import TopApiClient, TopException
# Ebay
from ebaysdk.finding import Connection as Finding

#######################################
# Data Imports#
from .secrets import *
from .models import Product
from .serializer import *


def call_Ebay(keyword):
    api = Finding(appid=EBAY_API_KEY, config_file=None)
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
        
def callApi_AliExpress(keyword):
    try:
        client = TopApiClient(
            appkey=ALIEXPRESS_APP_KEY,
            app_secret=ALIEXPRESS_API_KEY,
            top_gateway_url='http://api.taobao.com/router/rest',
            verify_ssl=False
        )

        page_number = 1
        all_products = []

        while True:
            request_dict = {
                "app_signature": "Marekti",
                "keywords": keyword,
                "page_no": str(page_number),
                "target_currency": "USD",
                "target_language": "en",
                "tracking_id": "Marketi",
            }

            file_param_dict = {}
            response = client.execute(
                "aliexpress.affiliate.product.query", request_dict, file_param_dict)

            if 'error_response' in response:
                error_message = response['error_response'].get('sub_msg') or response['error_response'].get('msg')
                raise Exception(f"AliExpress API Error: {error_message}")

            current_page_products = response.get('resp_result').get('result').get('products')

            if not current_page_products:
                # No more products on this page, break the loop
                break

            all_products.extend(current_page_products)
            page_number += 1

        serializer = AliExpressProductSerializer(all_products, many=True)
        return serializer.data

    except TopException as e:
        return f"AliExpress API Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"



def callApi_Rapid_AmazonApi(keyword):
    print("ee")
    try:
        url = "https://amazon23.p.rapidapi.com/product-search"

        page = 1  # Starting page number
        limit = 20  # Number of results per page

        all_products = []  # List to store all products

        def fetch_products(page):
            querystring = {"query": keyword, "page": page, "limit": limit}

            headers = {
                "X-RapidAPI-Key": RAPID_API_KEY,
                "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            if statusCheck(response):
                print("status check")
                return statusCheck(response)

            products = response.json().get('result')

            if not products:
                return  # No more products available

            all_products.extend(products)

            fetch_products(page + 1)  # Fetch next page recursively

        fetch_products(page)

        serializer = AmazonRapidProductSerializer(all_products, many=True)
        print(serializer.data)
        return serializer.data

    except Exception as e:
        return e

def callApi_Rapid_Shein(keyword):
    try:
        url = "https://unofficial-shein.p.rapidapi.com/products/search"

        querystring = {"keywords": keyword, "language": "en", "country": "US", "currency": "USD"}

        headers = {
            'X-RapidAPI-Key': RAPID_API_KEY,
            'X-RapidAPI-Host': 'unofficial-shein.p.rapidapi.com'
        }

        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            products = response.json().get('info').get("products")
            serializer = SheinRapidProductSerializer(products, many=True)
            return serializer.data
        else:
            return f"Error: {response.status_code}"
        
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except ValueError as e:
        return f"Error parsing JSON response: {e}"
    except Exception as e:
        return f"Unknown error occurred: {e}"


def callApi_Rapid_RealTime(keyword):
    try:
        url = "https://real-time-product-search.p.rapidapi.com/search"

        querystring = {"q": keyword, "country": "us", "language": "en"}

        headers = {
            'X-RapidAPI-Key': "5d35771659msh1de8eff53abd5afp14756fjsn875eab81aa56",
            'X-RapidAPI-Host': 'real-time-product-search.p.rapidapi.com'
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        
        if(statusCheck(response)):
            return statusCheck(response)
        
        products = response.json().get('data')
        serializer = RealTimeProductSerializer(products, many=True)
        return serializer.data
        # return products

    except Exception as e:
        return e


apiDec = {
    "AliExpress": callApi_AliExpress,
    "Ebay": call_Ebay,
    "Amazon": callApi_Rapid_AmazonApi,
    "RealTime": callApi_Rapid_RealTime,
    "Shein": callApi_Rapid_Shein,
}


def statusCheck(response):
     print(response.status_code)
     if response.status_code != 200:
            print("Error: " + str(response.status_code))

            return "Error: " + str(response.status_code)

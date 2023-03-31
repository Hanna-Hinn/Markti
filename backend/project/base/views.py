
#######################################
          #Rest Framework Imports#
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#######################################
            #Python Imports#
import requests


#######################################
            #Api Imports#
#AliExpress
from topsdk.client import TopApiClient, TopException
#Ebay
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

#######################################
            #Data Imports#
from .secrets import *
from .models import Product
from .serializer import *
from .stores_api import call_Ebay

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
    search = request.query_params.get('keyword')
    products = call_Ebay(search)
    # serialized_data = RealTimeProductSerializer(data = products, many=True)
    # serialized_data.is_valid(raise_exception=True)
    # deserialized_data = ProductSerializer(data=serialized_data.validated_data, many=True)
    # deserialized_data.is_valid(raise_exception=True)
    print(type(products))
    return Response(products)

@api_view(['POST'])
def createTicket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getTickets(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getTicket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    serializer = TicketSerializer(ticket)
    return Response(serializer.data)


@api_view(['PATCH','DELETE'])
def modifyTicket(request,modify,pk):    
    try:
        instance = Ticket.objects.get(pk=pk)
        if(request.method == "PATCH" and modify == "update"):
            serializer = TicketSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE" and modify=="delete":
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def getAPIs(request):
    apis = API.objects.all()
    serializer = APISerializer(apis, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createAPI(request):
    serializer = APISerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def getAPI(request, pk):
    api = API.objects.get(pk=pk)
    serializer = APISerializer(api)
    return Response(serializer.data)

@api_view(['PATCH','DELETE'])
def modifyAPI(request,modify,pk):    
    try:
        instance = API.objects.get(pk=pk)
        if(request.method == "PATCH"):
            serializer = APISerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except API.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
###############################
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsByStore(request, store):
    products = Product.objects.filter(store=store)
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsByCategory(request, category):
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsBySubCategory(request, subcategory):
    products = Product.objects.filter(subCategory=subcategory)
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsByBrand(request, brand):
    products = Product.objects.filter(brand=brand)
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsByPrice(request, price):
    products = Product.objects.filter(price=price)
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsByRating(request, rating):
    products = Product.objects.filter(rating=rating)
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductsByDiscount(request, discount):
    products = Product.objects.filter(discount=discount)
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def productCount(request):
    productCount = Product.objects.all().count()
    return Response(productCount)

@api_view(['GET'])
def productCountFromStore(request, store):
    productCount = Product.objects.filter(store=store).count()
    return Response(productCount)

@api_view(['GET'])
def productCountFromCategory(request, category):
    productCount = Product.objects.filter(category=category).count()
    return Response(productCount)

@api_view(['GET'])
def productCountFromSubCategory(request, subcategory):
    productCount = Product.objects.filter(subCategory=subcategory).count()
    return Response(productCount)

###############################


###########################
# Function : callApi
# Input : request , keyword(Search String)
# Output : Response (mostly Json)
# Description :
# ----------------------------
#  This function is used to call the APIs and return the data in Json format
# ----------------------------
###########################

# pip install ebaysdk
@api_view(['GET'])
def callApi_Ebay(request, keyword):
    
        api = Finding(appid= EBAY_API_KEY , config_file=None)
        api_request = {'keywords': keyword}
        try:
            response = api.execute('findItemsAdvanced', api_request)
            json_response = response.dict()
            products = json_response.get('searchResult').get('item')
            serializer = EbayProductSerializer(products,many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(e)
        
@api_view(['GET'])
def callApi_Rapid_AliExpress(request,keyword):
        try: 
            client = TopApiClient(appkey= ALIEXPRESS_APP_KEY , app_sercet= ALIEXPRESS_API_KEY  ,
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
            return Response(serializer.data)
        
        except TopException as e:
            print(e)
            return Response("Error")
        
@api_view(['GET'])
def callApi_Rapid_AmazonApi(request,keyword):
        try:
    
            url = "https://amazon23.p.rapidapi.com/product-search"

            querystring = {"query":keyword}

            headers = {
                "X-RapidAPI-Key": RAPID_API_KEY,
                "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            products = response.json().get('result')
            serializer = AmazonRapidProductSerializer(products,many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response("Error")
        
@api_view(['GET'])
def callApi_Rapid_Shein(request,keyword):
        try:
            url = "https://unofficial-shein.p.rapidapi.com/products/search"

            querystring = {"keywords":keyword,"language":"en","country":"US","currency":"USD"}

            headers = {
                'X-RapidAPI-Key': RAPID_API_KEY,
                'X-RapidAPI-Host': 'unofficial-shein.p.rapidapi.com'
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            products = response.json().get('info').get("products")
            serializer = SheinRapidProductSerializer(products,many=True)
            return Response(serializer.data)

        except Exception as e:
            print(e)
            return Response("Error")
        
@api_view(['GET'])
def callApi_Rapid_RealTime(request,keyword):     
    try:
        url = "https://real-time-product-search.p.rapidapi.com/search"

        querystring = {"q":keyword,"country":"us","language":"en"}

        headers = {
            'X-RapidAPI-Key': RAPID_API_KEY,
            'X-RapidAPI-Host': 'real-time-product-search.p.rapidapi.com'
            }

        response = requests.request("GET", url, headers=headers, params=querystring) 
        products = response.json().get('data')
        serializer = RealTimeProductSerializer(products,many=True)
        return Response(serializer.data)
        
    except Exception as e:
        print(e)
        return Response("Error")

apiDec = {
    "AliExpress":callApi_Rapid_AliExpress,
    "Ebay":callApi_Ebay,
    "Amazon":callApi_Rapid_AmazonApi,
    "RealTime" : callApi_Rapid_RealTime,
    "callApi_Rapid_Shein" : callApi_Rapid_Shein,
}
    





#######################################
          #Rest Framework Imports#
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#######################################
            #Python Imports#
#######################################
            #Data Imports#

from .serializer import *
from .stores_api import call_Ebay
from . import launcher 


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

@api_view(['Get'])
def start_launcher(request):
    # make list with fakestore  
    storeList = ["Ebay"]

    finalResultJason =json.dumps(launcher.launch(storeList, request.query_params.get('keyword')))
    return Response(finalResultJason)

# API_Dectionary = {
#         "Rapid_Amazon" :        callApi_Rapid_AmazonApi, 
#         "Rapid_AliExpress":     callApi_Rapid_AliExpress, 
#         "Ebay":                 callApi_Ebay, 
#         "FakeStore":            callApi_FakeStore ,
#         "Rapid_Shein":          callApi_Rapid_SheinAPI
#         }



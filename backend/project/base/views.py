
#######################################
# Rest Framework Imports#

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#######################################
# Python Imports#
#######################################
# Data Imports#

from .serializer import *
from .stores_api import *
from . import launcher
from . import pagenationManager

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
    products = callApi_Rapid_AmazonApi(search)
   # products = call_Ebay(search)
    # serialized_data = RealTimeProductSerializer(data = products, many=True)
    # serialized_data.is_valid(raise_exception=True)
    # deserialized_data = ProductSerializer(data=serialized_data.validated_data, many=True)
    # deserialized_data.is_valid(raise_exception=True)

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
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTicket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    serializer = TicketSerializer(ticket)
    return Response(serializer.data)


@api_view(['PATCH', 'DELETE'])
def modifyTicket(request, modify, pk):
    try:
        instance = Ticket.objects.get(pk=pk)
        if (request.method == "PATCH" and modify == "update"):
            serializer = TicketSerializer(
                instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE" and modify == "delete":
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


@api_view(['PATCH', 'DELETE'])
def modifyAPI(request, modify, pk):
    try:
        instance = API.objects.get(pk=pk)
        if (request.method == "PATCH"):
            serializer = APISerializer(
                instance, data=request.data, partial=True)
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
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsByStore(request, store):
    products = Product.objects.filter(store=store)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsByCategory(request, category):
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsBySubCategory(request, subcategory):
    products = Product.objects.filter(subCategory=subcategory)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsByBrand(request, brand):
    products = Product.objects.filter(brand=brand)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsByPrice(request, price):
    products = Product.objects.filter(price=price)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsByRating(request, rating):
    products = Product.objects.filter(rating=rating)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsByDiscount(request, discount):
    products = Product.objects.filter(discount=discount)
    serializer = ProductSerializer(products, many=True)
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
    """
    This function is to start the launcher
    Stores are passed as a list of strings (Store Names)

    """
    # make list with fakestore

    storeList = request.query_params.get('storeList').split(',')
    keyword = request.query_params.get('keyword')
    sortType = request.query_params.get('sortType')
    sortAscending = request.query_params.get('sortAscending')
    currencyType = request.query_params.get('currencyType')

    # res,
    res = launcher.launch(storeList, keyword, sortType,
                          sortAscending, currencyType)

    serializer = ProductSerializer(res, many=True)

    return Response(serializer.data)


# API_Dectionary = {
#         "Amazon" :        callApi_Rapid_AmazonApi,
#         "AliExpress":     callApi_Rapid_AliExpress,
#         "Ebay":                 callApi_Ebay,
#         "FakeStore":            callApi_FakeStore ,
#         "Shein":          callApi_Rapid_SheinAPI
#         }
###############################

@api_view(['Get'])
def get_Numberof_Pages(request):  # to return number of pages for FRONTEND
    """
    This function is to return the number of pages
    """
    return pagenationManager.get_total_pages()


@api_view(['Get'])
def get_Page(request):  # to return the data page for FRONTEND
    """
    This function is to return the data page
    """
    return pagenationManager.paginate(request.query_params.get('page'))


# make a view that takes the product list and return the number of pages
@api_view(['POST'])
# to return number of pages for FRONTEND
def get_Number_of_Pages_from_list(request):
    """
    This function is to return the number of pages
    """

    productList = request.data

    pageNumber = int(request.query_params.get('pageNumber'))
    return Response(pagenationManager.paginate(productList, pageNumber, 20))


@api_view(['GET'])
def callApi_Rapid_AliExpress(request):
    try:
        client = TopApiClient("34256468", "d7bf58da23cf6595d9b416323e3de3f4",
                              top_gateway_url='http://api.taobao.com/router/rest', verify_ssl=False)

        request_dict = {
            "app_signature": "Marekti",
            "keywords": "laptop",
            "page_no": "1",
            "target_currency": "USD",
            "target_language": "en",
            "tracking_id": "Marketi",
        }

        file_param_dict = {}
        response = client.execute(
            "aliexpress.affiliate.product.query", request_dict, file_param_dict)
        products = response.get('resp_result').get('result').get('products')
        serializer = AliExpressProductSerializer(products, many=True)
        return Response(serializer.data)

    except TopException as e:
        print(e)
        return Response("Error")

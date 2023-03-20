from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product

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
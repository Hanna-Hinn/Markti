from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('search/', views.search, name="search"),
    path('tickets/', views.getTickets, name="tickets"),
    path('tickets/create', views.createTicket, name="createTicket"),
    path('tickets/<str:pk>', views.getTicket, name="ticket"),
    path('tickets/<str:modify>/<str:pk>', views.modifyTicket, name="modifyTicket"),
    path('apis/', views.getAPIs, name="apis"),
    path('apis/create', views.createAPI, name="createAPI"),
    path('apis/<str:pk>', views.getAPI, name="api"),
    path('apis/<str:modify>/<str:pk>', views.modifyAPI, name="modifyAPI"),
]

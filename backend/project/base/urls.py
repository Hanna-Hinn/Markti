from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    path('search/', views.search, name="search"),

    path('tickets', views.getTickets, name="tickets"),
    path('tickets/create', views.createTicket, name="createTicket"),
    path('tickets/<int:pk>', views.getTicket, name="ticket"),
    path('tickets/<str:modify>/<int:pk>',
         views.modifyTicket, name="modifyTicket"),

    path('apis', views.getAPIs, name="apis"),
    path('apis/create', views.createAPI, name="createAPI"),
    path('apis/<int:pk>', views.getAPI, name="api"),
    path('apis/<str:modify>/<int:pk>', views.modifyAPI, name="modifyAPI"),

    path('start/', views.start_launcher, name="start_launcher"),
    path('page/', views.get_Number_of_Pages_from_list, name="GetPageNumber"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

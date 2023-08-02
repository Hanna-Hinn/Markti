from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # This path was made for testing.
    #path('search/', views.search, name="search"),

    # Tickets Paths
    path('tickets', views.getTickets, name="tickets"),
    path('reviews', views.getReviewTickets, name="reviews"),
    path('top-reviews', views.getTopReviews, name="top-reviews"),
    path('tickets/create', views.createTicket, name="createTicket"),
    path('tickets/<int:pk>', views.getTicket, name="ticket"),
    path('tickets/<str:modify>/<int:pk>',
         views.modifyTicket, name="modifyTicket"),
    
    # APIs model paths
    path('apis', views.getAPIs, name="apis"),
    path('apis/create', views.createAPI, name="createAPI"),
    path('apis/<int:pk>', views.getAPI, name="api"),
    path('apis/<str:modify>/<int:pk>', views.modifyAPI, name="modifyAPI"),

    # Path that will do the search and fetch products
    path('start/', views.start_launcher, name="start_launcher"),
    # This path will return products based on pages
    path('page/', views.get_Number_of_Pages_from_list, name="GetPageNumber"),

    # This path will return a list of stores.
    path('stores', views.getStores, name="listStores"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # adding the media urls and paths.

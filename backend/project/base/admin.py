from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Review)
admin.site.register(API)
admin.site.register(APIMethods)
admin.site.register(Ticket)
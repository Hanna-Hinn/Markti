from django.db import models
from django.contrib.auth.models import User


"""
    models.py:
        A model is the single, definitive source of information about your data. 
        It contains the essential fields and behaviors of the data you're 
        storing. Generally, each model maps to a single database table.
"""

# Store Model
class Store(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    # _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    productName = models.CharField(max_length=200, null=False, blank=False)
    storeProductID = models.CharField(max_length=200, null=True, blank=True)
    productPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    productImageURL = models.URLField(max_length=500, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    subCategory = models.CharField(max_length=200, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    discount = models.CharField(max_length=200, null=True, blank=True)
    productURL = models.CharField(max_length=200, null=True, blank=True)
    DisplayFields = ['productName','storeProductID','productPrice','rating','numReviews','category','brand','store','discount','productURL']
    SearchFields = ['productName','storeProductID','productPrice','rating','category','brand','store']
    FilterFields = ['storeProductID','category','brand','store']

    def __str__(self):
        return self.productName

# Review Model
class Review(models.Model):
    rating = models.IntegerField(null=True, blank=True, default=0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Product : " + str(self.product) + "// Rating : " + str(self.rating)

# API Model
class API(models.Model):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    mainURL = models.URLField(max_length=200, null=False, blank=False)
    includeSDK = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    DisplayFields = ['store','name','mainURL','includeSDK']
    SearchFields = ['store','name']
    FilterFields = ['store','mainURL','includeSDK']

    def __str__(self):
        return self.name

    @property
    def methods(self):
        return APIMethods.objects.get(mainAPI=self)

# API Methods Model
class APIMethods(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    method = models.CharField(max_length=200, null=True, blank=True)
    header = models.JSONField(null=True, blank=True)
    params = models.JSONField(null=True, blank=True)
    auth = models.JSONField(null=True, blank=True)
    body = models.JSONField(null=True, blank=True)
    mainAPI = models.ForeignKey(API, on_delete=models.SET_NULL, null=True)
    DisplayFields = ['name','url','method','mainAPI']
    SearchFields = ['name','url','method','mainAPI']
    FilterFields = ['url','method','mainAPI']

    def __str__(self):
        return "API : " + str(self.mainAPI) + "// Method : " + str(self.name)


# Ticket Model
class Ticket(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    userCreated = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    DisplayFields = ['id','type','rating','description','createdAt','userCreated','status']
    SearchFields = ['id','type','userCreated','status']
    FilterFields = ['type','userCreated','status']
    def __str__(self):
        return self.name

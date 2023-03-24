from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    # _id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return self.name


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
    Store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.productName


class Review(models.Model):
    rating = models.IntegerField(null=True, blank=True, default=0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Product : " + str(self.product) + "// Rating : " + str(self.rating)


class API(models.Model):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    mainURL = models.URLField(max_length=200, null=False, blank=False)
    includeSDK = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class APIMethods(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    method = models.CharField(max_length=200, null=True, blank=True)
    header = models.JSONField(null=True, blank=True)
    params = models.JSONField(null=True, blank=True)
    auth = models.JSONField(null=True, blank=True)
    body = models.JSONField(null=True, blank=True)
    mainAPI = models.ForeignKey(API, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "API : " + str(self.mainAPI) + "// Method : " + str(self.name)


class Ticket(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    userCreated = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

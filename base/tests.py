from django.test import TestCase
from .Objects.Product import Product
from .currencyConverter import convertCurrency
import requests
from unittest.mock import patch
from .sorter import sortAlphabit, sortRating, sortPrice, checkSortType



# Product.py tests
class ProductTestCase(TestCase):

    def setUp(self):
        # Create a sample product instance for testing
        self.product_data = {
            'product_id': 1,
            'product_title': 'Test Product',
            'product_category': 'Test Category',
            'product_image': 'test_image.jpg',
            'product_url': 'https://example.com',
            'product_price': 99.99,
            'product_rating': 4.5,
            'product_store': 'Test Store',
            'product_storeImage': 'store_image.jpg',
            'product_description': 'Test description',
            'product_trusted': True,
        }
        self.product = Product(**self.product_data)

    def test_product_str(self):
        # Test the __str__ method of the Product class
        expected_str = f"Product ID: {self.product_data['product_id']}, Product Title: {self.product_data['product_title']}, Product Category: {self.product_data['product_category']}, Product Image: {self.product_data['product_image']}, Product URL: {self.product_data['product_url']}, Product Price: {self.product_data['product_price']}, Product Rating: {self.product_data['product_rating']}"
        self.assertEqual(str(self.product), expected_str)

    def test_product_attributes(self):
        # Test the attributes of the product instance
        self.assertEqual(self.product.product_id, self.product_data['product_id'])
        self.assertEqual(self.product.product_title, self.product_data['product_title'])
        self.assertEqual(self.product.product_category, self.product_data['product_category'])
        self.assertEqual(self.product.product_image, self.product_data['product_image'])
        self.assertEqual(self.product.product_url, self.product_data['product_url'])
        self.assertEqual(self.product.product_price, self.product_data['product_price'])
        self.assertEqual(self.product.product_rating, self.product_data['product_rating'])
        self.assertEqual(self.product.product_store, self.product_data['product_store'])
        self.assertEqual(self.product.product_storeImage, self.product_data['product_storeImage'])
        self.assertEqual(self.product.product_description, self.product_data['product_description'])
        self.assertEqual(self.product.product_trusted, self.product_data['product_trusted'])

#######################################################################################################################


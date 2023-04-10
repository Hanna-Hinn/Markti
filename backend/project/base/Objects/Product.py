class Product:

 
    def __init__(self, product_id=None, product_title=None, product_category=None, product_image=None, product_url=None, product_price=None, product_rating=None):
        self.product_id = product_id
        self.product_title = product_title
        self.product_category = product_category
        self.product_image = product_image
        self.product_url = product_url
        self.product_price = product_price
        self.product_rating = product_rating

    def __str__(self):
        return f"Product ID: {self.product_id}, Product Title: {self.product_title}, Product Category: {self.product_category}, Product Image: {self.product_image}, Product URL: {self.product_url}, Product Price: {self.product_price}, Product Rating: {self.product_rating}"
    
    def __lt__(self, other):
        # Compare products based on their prices
        return self.product_price < other.product_price
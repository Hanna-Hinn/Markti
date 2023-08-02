class Product:

 
    def __init__(self,product_trusted=None,product_description=None,product_id=None, product_title=None, product_category=None, product_image=None, product_url=None, product_price=None, product_rating=None, product_store=None, product_storeImage=None):
        self.product_id = product_id
        self.product_title = product_title
        self.product_category = product_category
        self.product_image = product_image
        self.product_url = product_url
        self.product_price = product_price
        self.product_rating = product_rating
        self.product_store = product_store
        self.product_storeImage = product_storeImage
        self.product_description= product_description
        self.product_trusted = product_trusted


    def __str__(self):
        return f"Product ID: {self.product_id}, Product Title: {self.product_title}, Product Category: {self.product_category}, Product Image: {self.product_image}, Product URL: {self.product_url}, Product Price: {self.product_price}, Product Rating: {self.product_rating}"
    
  
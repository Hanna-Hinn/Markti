class Product:
    def __init__(self, name, price, rating, description, images, link, website):
        self._name = name
        self._price = price
        self._rating = rating
        self._description = description
        self._images = images
        self._link = link
        self._website = website

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def rating(self):
        return self._rating

    @property
    def description(self):
        return self._description

    @property
    def images(self):
        return self._images

    @property
    def link(self):
        return self._link

    @property
    def website(self):
        return self._website

    @name.setter
    def name(self, name):
        self._name = name

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price must be non-negative")
        self._price = price
    
    @rating.setter
    def rating(self, rating):
        if not isinstance(rating, (int, float)):
            raise TypeError("Rating must be a number")
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        self._rating = rating
    
    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if len(description) > 1000:
            raise ValueError("Description is too long")
        self._description = description
    
    @images.setter
    def images(self, images):
        self._images = images
    
    @link.setter
    def link(self, link):
        self._link = link
    
    @website.setter
    def website(self, website):
        self._website = website

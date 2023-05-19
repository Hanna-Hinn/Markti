
def filterTrusted(productList):
    """Filter the list of products to only include trusted products"""
    return productList,productList.filter(product_rating =True)

def filterUntrusted(productList):
    """Filter the list of products to only include untrusted products"""
    return productList,productList.filter(product_rating =False)

def filterStore(productList, store):
    """Filter the list of products to only include products from a specific store"""
    
    return productList,productList.filter(product_store=store)






    
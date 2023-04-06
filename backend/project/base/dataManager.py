from . import variables
from .Objects import Product
import time
import json

import json

def objectifyThread():
   
    nubmerOfObjectified = 0
    while True:
        time.sleep(1)
        if variables.dataQueue.empty():
            pass
        else: 
            currentData = variables.dataQueue.get()
  
            print (type(currentData))
        
            var_map = {
                "id": "product_id",
                "title": "product_title",
                "category": "product_category",
                "image": "product_image",
                "url": "product_url",
                "price": "product_price",
                "topRatedListing": "product_rating"
            }
            for item in currentData:
                for key, value in item.items():# value of the item is the value of the attribute

                    product = Product()

                    if key in variables.attributeDict:
                        var_name = var_map.get(key)
                        if var_name:
                            setattr(product, var_name, value)
                        
                    variables.informationList.append(product)

            nubmerOfObjectified +=1 # this adds one to the number of objectified
            variables.InformationQueue.put(variables.informationList)
            variables.informationList.clear()


            # check if the number of objectified is equal to the requested amount
            if nubmerOfObjectified == variables.requestedApiAmount:
                break
 


def myMainThread(): 
###########################
# Function : myMainThread
# Input :  None
# Output : None

# Description :
# ----------------------------
# This function is the main thread of the program.
# It will sort the results and print them.
# until the number of sorted results is equal to the number of requested apis.
# ----------------------------
###########################

    sortedResults = []
    numberOfSorted = 0
    while True:

        # wait to receive data 
        time.sleep(1)

        #wait for the informationQueue to have at least one item in it.
        if variables.InformationQueue.empty():
            pass
        else:
            # sort the results 
            with variables.results_lock:
                if variables.results != []:
                    print("Recived", variables.results)
                    print("Sorting...")
                    # sort the results according to the price
                    sortedResults = sorted(sortedResults + variables.results, key=lambda x: x.price)
                    variables.results.clear()
                    print("Sorted :", sortedResults)
                    numberOfSorted +=1
        
        if numberOfSorted == variables.requestedApiAmount:
            #kill thread and print the results 
            return sortedResults

            

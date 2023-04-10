from . import variables
from .Objects.Product import Product
import time




def objectifyThread():
   
    nubmerOfObjectified = 0
    while True:
        time.sleep(1)
        if variables.dataQueue.empty():
            pass
        else: 
            itemList = variables.dataQueue.get()
           

            attributeDict = {
                    #for Ebay
                    "itemId": {"id": "product_id"},
                    "title": {"title": "product_title"},
                    "categoryName": {"category": "product_category"},
                    "galleryURL": {"image": "product_image"},
                    "viewItemURL": {"url": "product_url"},
                    "value": {"price": "product_price"},
                    "topRatedListing": {"topRatedListing": "product_rating"},
                    #
                }
        
            print("Objectifying...")
        # THIS IS COMPLECATED ASK ME LATER
            try:

                for item in itemList:
                    # Create a Product object
                    product = Product()
                    # Nested dictionary iteration
                    for key, value in item.items():
                 
                        
                        # Iterate over attributeDict dictionary
                        for attribute, attributeValue in attributeDict.items():
                            if key == attribute:
                                for attributeKey,attributeResult in attributeValue.items():
                                   

                                    # Set attribute on the Product object
                                    setattr(product, str(attributeResult), str(value))
                                    
                                   
                    # print(product)

                    # Append the Product object to the queue
                    variables.informationList.append(product)
                
             
            except Exception as e:
                print("Error in objectifyThread", e)

            nubmerOfObjectified +=1 # this adds one to the number of objectified
            variables.InformationQueue.put(variables.informationList)
            


            # check if the number of objectified is equal to the requested amount
            if nubmerOfObjectified == variables.requestedApiAmount:
                print("finshed objectifying")
                print(variables.InformationQueue.qsize())
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
    print("Starting main thread")
    sortedResults = []
    numberOfSorted = 0
    while True:

        

        # wait to receive data 
        time.sleep(1)

        #wait for the informationQueue to have at least one item in it.
        if variables.InformationQueue.empty():
            print("Waiting for informationQueue to have at least one item in it.")
        else:
            # sort the results 
            variables.results = variables.InformationQueue.get()
            if variables.results != []:
                print("Recived",len(variables.results),"results")
                print("Sorting...")
                # sort the results according to the price
                sortedResults = sorted(sortedResults + variables.results)

               
             
                numberOfSorted +=1
        
        if numberOfSorted == variables.requestedApiAmount:
            #kill thread and print the results 
            variables.results = sortedResults
            print("finshed sorting")
            print("finshed main thread")
            break

            

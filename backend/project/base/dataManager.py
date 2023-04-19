from . import variables
from .Objects.Product import Product
import time




def objectifyThread():
###########################
# Function : objectifyThread
# Input :  None
# Output : None

# Description :
# ----------------------------
# This function is used to objectify the data from the dataQueue
# and then put it in the informationlist then will be added to informationQueue
# ----------------------------
###########################
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
# It waits for the informationQueue to have at least one item in it.
# Then it sorts the results according to the price.
# Then it prints the results.
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
                for result in variables.results:
                    if result.product_price == None: # if the price is None then set it to 0
                        result.product_price = 0
                    else:
                        result.product_price = float(result.product_price) # convert the price to a float
                # sort the results
                # add dummy results to the sortedResults list
               

                sortedResults = sortedResults  + variables.results
                
                sortedResults = sorted(sortedResults, key=lambda x: x.product_price)

                for result in sortedResults:
                    #print pice
                    print(result.product_price)
           
                numberOfSorted +=1
        
        if numberOfSorted == variables.requestedApiAmount:
            #kill thread and print the results 
            variables.results = sortedResults
            print("finshed sorting")
            print("finshed main thread")
            break

            

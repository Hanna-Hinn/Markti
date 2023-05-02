
from .Objects.Product import Product
from .Objects.VariablesDTO import VariablesDTO
import time
import os



def objectifyThread(var_dto: VariablesDTO):
    """
    Function 
    This function takes the data from the dataQueue and objectifies it into a Product object
    and then adds it to the informationList
    Args:
    -----
        None
    Returns:
    --------
        None
    """
 
    while True:
        time.sleep(1)
        if var_dto.dataQueue.empty():
            pass
        else: 
            # get the store name from the dataQueue sent as [storeName,result]
            data = var_dto.dataQueue.get()
            storeName =  data [0]
          
            itemList = data [1]
           

            attributeDict = {
                # AS IN THE SERIALIZER
                    #for Ebay
                    "itemId": {"id": "product_id"},
                    "title": {"title": "product_title"},
                    "categoryName": {"category": "product_category"},
                    "galleryURL": {"image": "product_image"},
                    "viewItemURL": {"url": "product_url"},
                    "value": {"price": "product_price"},
                    "topRatedListing": {"topRatedListing": "product_rating"},
                    #for Amazon
                    "asin": {"id": "product_id"},
                    "current_price": {"price": "product_price"},
                    "total_reviews": {"total_reviews": "product_rating"},
                    "rating": {"rating": "product_rating"},
                    "url": {"url": "product_url"},
                    "amazonChoice": {"amazonChoice": "product_amazonChoice"},
                    "bestSeller": {"bestSeller": "product_bestSeller"},
                    "amazonPrime": {"amazonPrime": "product_amazonPrime"},
                    "title": {"title": "product_title"},
                    "thumbnail": {"image": "product_image"},
                    #
                    #for AliExpress
                    "product_id": {"id": "product_id"},
                    "first_level_category_name": {"category": "product_category"},
                    "original_price": {"price": "product_price"},
                    "product_detail_url": {"url": "product_url"},
                    "product_main_image_url": {"image": "product_image"},
                    "product_title": {"title": "product_title"},
                    "promotion_link": {"promotion_link": "product_promotion_link"},
                    #
                    #for Shein   

                    "goods_sn": {"id": "product_id"},
                    "goods_img": {"image": "product_image"},
                    "goods_name": {"title": "product_title"},
                    "usdAmountWithSymbol": {"price": "product_price"},
                    "comment_num": {"total_reviews": "product_rating"},
                   

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
                                    setattr(product, "product_store", storeName)
                                    path = "http://127.0.0.1:8000/static/images/"+ storeName +".png"
                                    setattr(product, "product_store_image", path)
                                   
                    

                    # Append the Product object to the queue
                    var_dto.informationList.append(product)
                
             
            except Exception as e:
                print("Error in objectifyThread", e)

            var_dto.nubmerOfObjectified +=1 # this adds one to the number of objectified
            var_dto.informationQueue.put(var_dto.informationList)
            


            # check if the number of objectified is equal to the requested amount
            if var_dto.nubmerOfObjectified == var_dto.requestedApiAmount:
                print("finshed objectifying")
                
                break
                
 


def myMainThread(var_dto: VariablesDTO): 
    """
    Function 
        this function is the main thread that will be running in the background
        it will be sorting the results and then adding them to the informationQueue
        this is done so that the informationQueue will always have the latest results
        and will be used by the pagenationManager to display the results
    Args:
        None
    Returns:
        None
    """
 
    print("Starting main thread")
  
    while True:

        

        # wait to receive data 
        time.sleep(1)

        #wait for the informationQueue to have at least one item in it.
        if var_dto.informationQueue.empty():
            print("Waiting for informationQueue to have at least one item in it.")
        else:
            # sort the results 
            var_dto.results = var_dto.informationQueue.get()
            if var_dto.results != []:
                print("Recived",len(var_dto.results),"results")
                print("Sorting...")
                # sort the results according to the price
                # why is this important? because the price is the only thing that is the same for all the apis
                for result in var_dto.results:
                    if result.product_price == None: # if the price is None then set it to 0
                        result.product_price = 0
                    else:
                        result.product_price = float(result.product_price) # convert the price to a float
                # sort the results
                # add dummy results to the sortedResults list
               

                var_dto.sortedResults = var_dto.sortedResults  + var_dto.results
                
                var_dto.sortedResults = sorted(var_dto.sortedResults, key=lambda x: x.product_price)
                
        
           
                var_dto.numberOfSorted +=1
        
        if var_dto.numberOfSorted == var_dto.requestedApiAmount and var_dto.requestedApiAmount !=0:
            #kill thread and print the results 
            var_dto.finshedresult = var_dto.sortedResults
            print("finshed sorting")
            print("finshed main thread")
            break
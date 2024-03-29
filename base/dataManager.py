

from .Objects.Product import Product
from .Objects.VariablesDTO import VariablesDTO
from . import sorter
from .import currencyConverter
import time


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
        if var_dto.error == "ALL APIS ARE EMPTY" and var_dto.requestedApiAmount == 0:
            break
       
        if var_dto.dataQueue.empty():
            pass
        else:
            # get the store name from the dataQueue sent as [storeName,result]
            data = var_dto.dataQueue.get()
            

            storeName = data[0]
            
            itemList = data[1]

            
            attributeDict = {
                "itemId": "product_id",
                "title": "product_title",

                "galleryURL": "product_image",
                "viewItemURL": "product_url",
                "value": "product_price",
                "topRatedListing": "product_trusted",
                "rating": "product_rating",

                "asin": "product_id",
                "current_price": "product_price",
                "total_reviews": "product_rating",

                "url": "product_url",
                "amazonChoice": "product_trusted",



                "thumbnail": "product_image",
                "product_id": "product_id",
                
                "original_price": "product_price",
                "promotion_link": "product_url",
                "product_main_image_url": "product_image",
                "product_title": "product_title",


                #shien
                "goods_id": "product_id",
                "goods_img": "product_image",
                "goods_url_name": "product_title",
                "generatedURL": "product_url",
                "usdAmountWithSymbol": "product_price",
                "comment_rank_average": "product_rating",
               

                # aliexpress
                "product_page_url": "product_url",
                "product_price": "product_price",
                "product_rating": "product_rating",
                "product_title": "product_title",
                "product_url": "product_url",
                "product_image": "product_image",
                "evaluate_rate": "product_rating",

                "store_rating": "product_trusted",


            }

            # print("Objectifying...")
            # THIS IS COMPLICATED ASK ME LATER
            try:
                for item in itemList:


                    # Error in objectifyThread 'Response' object is not iterable fix
                    if type(item) == str:
                        continue

                    # Create a Product object
                    product = Product()
                    for key, value in item.items():
                        attributeResult = attributeDict.get(key)
                        if attributeResult:
                            setattr(product, attributeResult, str(value))
                            setattr(product, "product_store", storeName)
                            path = "https://marketi-ps-caab34e05b6a.herokuapp.com/static/images/" + storeName + ".png"
                            setattr(product, "product_store_image", path)
                            if attributeResult == "product_image":
                                setattr(product, 'product_image', str(value).replace('http://', 'https://'))
                            
                        

                    # Append the Product object to the queue
                    var_dto.informationList.append(product)

            except Exception as e:
                var_dto.error = e
                print("Error in objectify Thread", e)

            var_dto.nubmerOfObjectified += 1  # this adds one to the number of objectified
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
   
    x=0

    while True:

        # wait to receive data
        time.sleep(1)

        # wait for the informationQueue to have at least one item in it.
        if var_dto.error == "ALL APIS ARE EMPTY" and var_dto.requestedApiAmount == 0:
            break
       

        if var_dto.informationQueue.empty():
            pass
            # print("Waiting for informationQueue to have at least one item in it.")
        else:
            var_dto.sortedResults = []
            # sort the results
            var_dto.results = var_dto.informationQueue.get()

            # check if the var_dto.error is true

            if var_dto.results != []:

                x += 1

                # sort the results according to the price
                # why is this important? because the price is the only thing that is the same for all the apis
                for result in var_dto.results:
                    if result.product_price == None:  # if the price is None then set it to 0
                        result.product_price = 0
                    else:
                        # convert the price to a float and remove $
                        result.product_price = float(str(result.product_price).replace("$", "").replace(",",""))
                # sort the results
                # add dummy results to the sortedResults list

                var_dto.sortedResults = var_dto.sortedResults + var_dto.results

                var_dto.sortedResults = sorter.checkSortType(
                    var_dto.sortType, var_dto.sortedResults, var_dto.sortAscending)

                var_dto.numberOfSorted += 1
            else:
                var_dto.numberOfSorted += 1


        if var_dto.numberOfSorted == var_dto.requestedApiAmount  :
            # kill thread and print the results

            currencyConverter.convertCurrency(
                var_dto.sortedResults, var_dto.currencyType)

            break

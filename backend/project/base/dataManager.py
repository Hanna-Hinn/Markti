
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
            storeName = data[0]

            itemList = data[1]

            attributeDict = {
                "itemId": "product_id",
                "title": "product_title",
                "categoryName": "product_category",
                "galleryURL": "product_image",
                "viewItemURL": "product_url",
                "value": "product_price",
                "topRatedListing": "product_rating",
                "asin": "product_id",
                "current_price": "product_price",
                "total_reviews": "product_rating",
                "rating": "product_rating",
                "url": "product_url",
                "amazonChoice": "product_amazonChoice",
                "bestSeller": "product_bestSeller",
                "amazonPrime": "product_amazonPrime",
                "thumbnail": "product_image",
                "product_id": "product_id",
                "first_level_category_name": "product_category",
                "original_price": "product_price",
                "product_detail_url": "product_url",
                "product_main_image_url": "product_image",
                "product_title": "product_title",
                "promotion_link": "product_promotion_link",
                "goods_sn": "product_id",
                "goods_img": "product_image",
                "goods_name": "product_title",
                "usdAmountWithSymbol": "product_price",
                "comment_num": "product_rating",
                "description": "product_description",
                "product_description": "product_description",
                "product_page_url": "product_url",
                "product_price": "product_price",
                "product_rating": "product_rating",
                "product_title": "product_title",
                "product_url": "product_url",
                "product_image": "product_image",

            }

            print("Objectifying...")
            # THIS IS COMPLICATED ASK ME LATER
            try:
                for item in itemList:
                    # Create a Product object
                    product = Product()
                    for key, value in item.items():
                        attributeResult = attributeDict.get(key)
                        if attributeResult:
                            setattr(product, attributeResult, str(value))
                            setattr(product, "product_store", storeName)
                            path = "http://127.0.0.1:8000/static/images/" + storeName + ".png"
                            setattr(product, "product_store_image", path)

                    # Append the Product object to the queue
                    var_dto.informationList.append(product)

            except Exception as e:
                print("Error in objectifyThread", e)

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

    print("Starting main thread")
    x = 1
    while True:

        # wait to receive data
        time.sleep(1)

        # wait for the informationQueue to have at least one item in it.
        if var_dto.informationQueue.empty():
            print("Waiting for informationQueue to have at least one item in it.")
        else:
            var_dto.sortedResults = []
            # sort the results
            var_dto.results = var_dto.informationQueue.get()

            if var_dto.results != []:

                if x == 2:
                    for i in var_dto.results:
                        print(i.product_id)

                x += 1
                print("Recived", len(var_dto.results), "results")
                print("Sorting...")
                # sort the results according to the price
                # why is this important? because the price is the only thing that is the same for all the apis
                for result in var_dto.results:
                    if result.product_price == None:  # if the price is None then set it to 0
                        result.product_price = 0
                    else:
                        # convert the price to a float
                        result.product_price = float(result.product_price)
                # sort the results
                # add dummy results to the sortedResults list

                var_dto.sortedResults = var_dto.sortedResults + var_dto.results

                var_dto.sortedResults = sorted(
                    var_dto.sortedResults, key=lambda x: x.product_price)

                var_dto.numberOfSorted += 1

        if var_dto.numberOfSorted == var_dto.requestedApiAmount and var_dto.requestedApiAmount != 0:
            # kill thread and print the results
            var_dto.finshedresult = var_dto.sortedResults
            print("finshed sorting")
            print("finshed main thread")
            break


def sortAlphabit(resultList, ascending: bool):
    """
    Function
        this function sorts the results according to the product title
    Args:
        resultList: list of results
        ascending: bool
    Returns:
        resultList: list of results
    """
    for result in resultList:
        if result.product_title == None:
            result.product_title = ""
    if ascending:
        resultList = sorted(resultList, key=lambda x: x.product_title)
    else:
        resultList = sorted(
            resultList, key=lambda x: x.product_title, reverse=True)
    return resultList


# function that sorts according to the rating
def sortRating(resultList, ascending: bool):
    """
    Function
        this function sorts the results according to the product rating
    Args:
        resultList: list of results
        ascending: bool
    Returns:
        resultList: list of results
    """
    for result in resultList:
        if result.product_rating == None:
            result.product_rating = 0
        else:
            result.product_rating = float(result.product_rating)
    if ascending:
        resultList = sorted(resultList, key=lambda x: x.product_rating)
    else:
        resultList = sorted(
            resultList, key=lambda x: x.product_rating, reverse=True)
    return resultList


def sortPrice(resultList, ascending: bool):
    """
    Function
        this function sorts the results according to the product price
    Args:
        resultList: list of results
        ascending: bool
    Returns:
        resultList: list of results
    """
    for result in resultList:
        if result.product_price == None:
            result.product_price = 0
        else:
            result.product_price = float(result.product_price)
    if ascending:
        resultList = sorted(resultList, key=lambda x: x.product_price)
    else:
        resultList = sorted(
            resultList, key=lambda x: x.product_price, reverse=True)
    return resultList

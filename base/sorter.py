
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
    if ascending == True:
        resultList = sorted(resultList, key=lambda x: x.product_title)
    else:
        resultList = sorted(resultList, key=lambda x: x.product_title, reverse=True)
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
    if ascending == True:
        resultList = sorted(resultList, key=lambda x: x.product_rating)
    else:
        resultList = sorted(resultList, key=lambda x: x.product_rating, reverse=True)
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
        resultList = sorted(resultList, key=lambda x: x.product_price, reverse=True)
      
        # print results
      

           
    return resultList

def checkSortType(sortType, resultList,sortAscending):
    

    if(sortType == "price"):
        sortType = sortPrice(resultList,sortAscending)
    elif(sortType == "rating"):
        sortType = sortRating(resultList,sortAscending)
    elif(sortType == "alphabit"):
        sortType = sortAlphabit(resultList,sortAscending)
    else:
        return "Wrong sort type"

    return sortType

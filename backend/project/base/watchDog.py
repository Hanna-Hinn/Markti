import threading as th
from . import storeApis as variables
from .Objects.VariablesDTO import VariablesDTO


def start(var_dto: VariablesDTO):
    """
    This function creates a thread for each store name in the storeList
    It then starts the thread and waits for it to finish
    adding the results to the dataQueue
    Parameters
    ----------
    storeList : list
        list of store names

    Returns
    -------
    None
    """
   # print("watchdog started")

    # loop through the function list

    # print("keyword:",var_dto.keyword,"\n")

    for storeName in var_dto.storeList:
        # check if the function is in variables.API_Dectionary
        if storeName in variables.API_Dectionary:
            # define a separate thread function for each store name
            def myThread(store):
                # get the corresponding function based on store name
                func = variables.API_Dectionary[store]

                # run the function and store the result
                print("keyword:", var_dto.keyword, "\n")
                result = func(var_dto.keyword)

                # send the store name and the result to the dataQueue
                # if the result is not a string (error) then send the result
                if (type(result) != str):
                    if (len(result) == 0):
                        var_dto.emptyApi += 1
                        var_dto.emptyApiList.append(store)
                      
                    else:
                        var_dto.dataQueue.put([store, result])
                else:
                    var_dto.dataQueue.put([store, "error"])

            # start a thread for each store name
            t = th.Thread(target=myThread, args=(storeName,))
            t.name = storeName

            t.start()
            # add the thread to the list
            var_dto.threads.append(t)
        else:
            # return an error if the function is not in variables.API_Dectionary
            var_dto.error = f"Error: {storeName} is not in variables.API_Dectionary"
            return f"Error: {storeName} is not in variables.API_Dectionary"


    # wait for all the threads to finish
    for t in var_dto.threads:
        t.join()
    print("requestedApiAmount(before empty check):", var_dto.requestedApiAmount)
    var_dto.requestedApiAmount = len(var_dto.storeList) - var_dto.emptyApi
    if var_dto.requestedApiAmount == 0:
        var_dto.error = "ALL APIS ARE EMPTY"
 
    # set the requestedApiAmount to the length of the function list
   
    print("requestedApiAmount(after checking if empty):", var_dto.requestedApiAmount)

    print("\n", "watchdog finished")

import threading as th
from . import variables



def Start(storeList):
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
    print("watchdog started")

    # clear the results list so if you spam the search button it will not return the results from the previous search
    variables.results.clear()

    
    # create a list to store the threads
    threads = []
    # loop through the function list
    # print storlsit
    print("keyword:",variables.keyWord,"\n")
   
    for storeName in storeList:
        # check if the function is in variables.API_Dectionary
        if storeName in variables.API_Dectionary:
            # define a separate thread function for each store name
            def myThread(store):
                # get the corresponding function based on store name
                func = variables.API_Dectionary[store]
                
                # run the function and store the result
                result = func(variables.keyWord)
                
                # send the store name and the result to the dataQueue
                variables.dataQueue.put([store, result])

            # start a thread for each store name
            t = th.Thread(target=myThread, args=(storeName,))
            t.name = storeName
            t.start()
            # add the thread to the list
            threads.append(t)
        else:
            # return an error if the function is not in variables.API_Dectionary
            return f"Error: {storeName} is not in variables.API_Dectionary"


        
    # set the requestedApiAmount to the length of the function list
    variables.requestedApiAmount = len(storeList)

    # wait for all the threads to finish
    for t in threads:
        t.join()
        
        print("\n","function finished: ",t.name ,"\n","queue size: ", variables.dataQueue.qsize() )

    print("\n","watchdog finished")

            

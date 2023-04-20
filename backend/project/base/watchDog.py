import threading as th
from . import variables



def Start(storeList):
    print("watchdog started")

    # clear the results list so if you spam the search button it will not return the results from the previous search
    variables.results.clear()

    
    # create a list to store the threads
    threads = []
    # loop through the function list
    for storeName in storeList:
      
        # check if the function is in variables.API_Dectionary
        if storeName in variables.API_Dectionary:
            # create a thread for the function
            def myThread():
                # run the function and store the result
                print("function started: ",storeName, "Keyword:",variables.keyWord)
                result = variables.API_Dectionary[storeName](variables.keyWord)
                # send the store name and the result to the dataQueue
           
                variables.dataQueue.put([storeName,result])
            
            # start the thread
            t = th.Thread(target=myThread)
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
        
        print("function finished: ",storeName, variables.keyWord ,"queue size: ", variables.dataQueue.qsize() )

    print("watchdog finished")

            

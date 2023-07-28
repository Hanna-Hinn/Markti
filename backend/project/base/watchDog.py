import threading as th
from . import storeApis
from .Objects.VariablesDTO import VariablesDTO

def start(var_dto: VariablesDTO):
    # Loop through the storeList
    for storeName in var_dto.storeList:
        # Check if the function is in variables.API_Dectionary
        func = storeApis.API_Dectionary.get(storeName, None)
        if func is not None:
            # Define a separate thread function for each store name
            def myThread(store):
                try:
                    # Run the function and store the result
                    print("keyword:", var_dto.keyword, "\n")
                    result = func(var_dto.keyword)

                    # Send the store name and the result to the dataQueue
                    # If the result is not a string (error), then send the result
                    print("result:", result, "\n")
                    if (type(result) != str):
                        if (len(result) == 0):
                            var_dto.emptyApi += 1
                            var_dto.emptyApiList.append(store)
                        else:
                            var_dto.dataQueue.put([store, result])
                    else:
                        var_dto.dataQueue.put([store, "error"])

                except Exception as e:
                    var_dto.error = f"Error: {str(e)}" + " in " + store +"thread"
                    return f"Error in threads: {str(e)}"

            # Start a thread for each store name
            t = th.Thread(target=myThread, args=(storeName,))
            t.name = storeName
            t.start()
            # Add the thread to the list
            var_dto.threads.append(t)
        else:
            # Return an error if the function is not in variables.API_Dectionary
            var_dto.error = f"Error: {storeName} is not in variables.API_Dectionary"
            return f"Error: {storeName} is not in variables.API_Dectionary"

    # Wait for all the threads to finish
    for t in var_dto.threads:
        t.join()

    print("requestedApiAmount(before empty check):", var_dto.requestedApiAmount)
    var_dto.requestedApiAmount = len(var_dto.storeList) - var_dto.emptyApi
    if var_dto.error == "":
            if var_dto.requestedApiAmount == 0:
                 var_dto.error = "ALL APIS ARE EMPTY"
    else:
        print("error:", var_dto.error)
        var_dto.requestedApiAmount = 0


    
        


    
    
    # Set the requestedApiAmount to the length of the function list
    print("requestedApiAmount(after checking if empty):", var_dto.requestedApiAmount)
    print("\n", "watchdog finished")

import threading as th
from . import variables

def Start(functionlist):

    # clear the results list so if you spam the search button it will not return the results from the previous search
    variables.results.clear()
    # create a list to store the threads
    threads = []
    # loop through the function list
    for fname in functionlist:
        # check if the function is in variables.API_Dectionary
        if fname in variables.API_Dectionary:
            # create a thread for the function
            def myThread():
                # run the function and store the result
                result = variables.API_Dectionary[fname]()
                print("eeeeeeeeeee")
                print(result)
                with variables.results_lock:
                    for i in result:
                      variables.results.append(i)
                    result.clear()
            
            # start the thread
            t = th.Thread(target=myThread)
            t.start()
            # add the thread to the list
            threads.append(t)
        else:
            # return an error if the function is not in variables.API_Dectionary
            return f"Error: {fname} is not in variables.API_Dectionary"

    # wait for all the threads to finish
    for t in threads:
        t.join()

    # set finished to True

    variables.finished = True
    
            

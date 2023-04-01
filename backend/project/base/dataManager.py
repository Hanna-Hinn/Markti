
import time


from . import variables

def myMainThread(): 
###########################
# Function : myMainThread
# Input :  None
# Output : None

# Description :
# ----------------------------
# This function will start the Main Thread.
# Starts watchDog and waits for it to finish.
# The Main Thread will sort the results from the watchDog.
# The function will keep waiting for data until the watchDog has finished.

# ----------------------------

# Future Changes :
# ----------------------------
# 1. Change the print statements to return statements.
# 2. Make it so that the function returns the sorted results.
# 3. Make it use queues instead of locks.
# 4. check for performance issuse in time.sleep
# ----------------------------

###########################
    # start the watchDog
    sortedResults = []

    while True:

        # wait to receive data # check for performance issuse
        time.sleep(1)

        # sort the results 
        with variables.results_lock:
            if variables.results != []:
                print("Recived", variables.results)
                print("Sorting...")
                # this by default sorts by the first element in the list using TimSort algorithm 
                sortedResults = sorted(sortedResults + variables.results) 
                variables.results.clear()
                print("Sorted :", sortedResults)
        # check if __finished sorting
        if variables.finished:
            # print the sorted results
            print("finshed")
            variables.results = sortedResults
            break
        else:
            # print the sorting progress
            print("Waiting....")



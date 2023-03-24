import threading
from .dataManager import dog_finished, data_SendToDataManager
from views import apiDec

class watchDog:
 
 ###########################
# Function : start_watchdog
# Input :    string_list(shop filters)
# Output :   None
# Description : 
# ----------------------------
#   This function is used to start the watchdog thread  
#   It takes a list of strings and checks if the string is in the apiDec dictionary
#   If it is it creates a thread and runs the function
#   It then joins the threads
#   It then calls the dog_finished function
# ----------------------------
###########################

    def start_watchdog(self, string_list):
        thread_list = []
        for string in string_list:
            if string in apiDec:
                func = apiDec[string]
                t = threading.Thread(target=self.run_func_and_send_to_dm, args=(func,))
                thread_list.append(t)
                t.start()
        
        for t in thread_list:
            t.join()
        
        dog_finished()


###########################
# Function : run_func_and_send_to_dm
# Input :    func(function to run)
# Output :   None
# Description : 
# ----------------------------
#   This function is used to run a function and send the data to the dataManager
# ----------------------------
###########################
    def run_func_and_send_to_dm(self, func):
        func()
        data_SendToDataManager()
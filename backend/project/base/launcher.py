
from threading import Thread
from . import watchDog

from . import dataManager
from . import variables 


def launch(storelist,keword):
   
    variables.keyWord = keword
    # start the main thread
    main_thread = Thread(target=dataManager.myMainThread)
    main_thread.start()
    #start the objectify 
    object_thread = Thread(target=dataManager.objectifyThread)
    object_thread.start()
    # start the watchDog
    watchDog.Start(storelist)
    # wait for the objectification to finsh
    object_thread.join()
    # wait for the main thread to finish before returning results
    main_thread.join()
    
    return variables.results

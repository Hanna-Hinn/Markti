
from threading import Thread
from . import watchDog

from . import dataManager
from . import variables 
from . import pagenationManager


def launch(storelist,keword):
    
    # clear the variables
    variables.results.clear()
    variables.dataQueue.queue.clear()
    variables.informationList.clear()
    variables.InformationQueue.queue.clear()
    variables.keyWord = keword

    # start the main thread
    main_thread = Thread(target=dataManager.myMainThread)
    main_thread.start()
    #start the objectify 
    object_thread = Thread(target=dataManager.objectifyThread)
    object_thread.start()
    # start the watchDog
    watchDog_thread= Thread(target=watchDog.Start(storelist))
    watchDog_thread.start()
    
    #wait for the objectify thread to finish
    watchDog_thread.join()
    
    object_thread.join()
    
    main_thread.join()
    
    
    return pagenationManager.paginate(1)


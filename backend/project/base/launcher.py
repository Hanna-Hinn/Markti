
from threading import Thread
from . import watchDog

from . import dataManager
from . import variables 


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
    print("here1")
    #wait for the objectify thread to finish
    watchDog_thread.join()
    print("here2")
    object_thread.join()
    print("here3")
    main_thread.join()
    print("here4")
    return variables.results

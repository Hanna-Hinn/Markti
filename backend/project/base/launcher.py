
from threading import Thread
from . import watchDog

from . import dataManager
from . import variables 
from . import pagenationManager


def launch(storelist,keyword):
    """
    This function is used to start all the main thread(the thread responsible for sorting the results)
    and the watchDog thread(the thread responsible for starting the threads for each store)
    it also starts the objectify thread(the thread responsible for converting the results to objects)
    and waits for the objectify thread to finish before returning the results

    Parameters
    ----------
    storelist : list
        list of store names
    keyword : str
        the keyword that the user entered
    
    Returns
    -------
    list
        list of objects

    """
    
    # clear the variables
    variables.results.clear()
    variables.dataQueue.queue.clear()
    variables.informationList.clear()
    variables.InformationQueue.queue.clear()
    variables.keyWord = keyword

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


from threading import Thread
from . import watchDog
from . import dataManager
from . import pagenationManager
from .Objects.VariablesDTO import VariablesDTO


def launch(storelist, keyword):
    """
    This function is used to start all the main thread (the thread responsible for sorting the results)
    and the watchDog thread (the thread responsible for starting the threads for each store)
    it also starts the objectify thread (the thread responsible for converting the results to objects)
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
    
    var_dto = VariablesDTO()
    
    var_dto.keyword = keyword
    var_dto.storeList = storelist
    
    # start the main thread
    main_thread = Thread(target=dataManager.myMainThread, args=(var_dto,))
    
    #start the objectify 
    object_thread = Thread(target=dataManager.objectifyThread, args=(var_dto,))
    
    #start the watchDog
    watchDog_thread= Thread(target=watchDog.start, args=(var_dto,))
    
    main_thread.start()
    
    object_thread.start()
    watchDog_thread.start()
    
    #wait for the objectify thread to finish
    watchDog_thread.join()
    object_thread.join()
    main_thread.join()
   
    
    return pagenationManager.paginate(var_dto.sortedResults, 1)

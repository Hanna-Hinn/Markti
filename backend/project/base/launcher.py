
from threading import Thread
from . import watchDog

from . import dataManager
from . import variables 


def launch(storelist):
   

    # start the main thread
    main_thread = Thread(target=dataManager.myMainThread)
    main_thread.start()
  
    # start the watchDog
    watchDog.Start(storelist)

    # wait for the main thread to finish before returning results
    
    main_thread.join()
    
    return variables.results

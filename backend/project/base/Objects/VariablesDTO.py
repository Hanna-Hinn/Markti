import queue

class VariablesDTO:
    def __init__(self,dataQueue=None,resultList=None,requestedApiAmount=None
                 ,informationList=None,informationQueue=None,sortedResults=None,
                 numberOfSorted=None,nubmerOfObjectified=None,keyword=None,storeList=None
                 ,threads=None,sortType=None,sortAscending=None,currencyType=None,error=None
                 ,emptyApi=None
                
                 ):
       

        self.dataQueue = queue.Queue()
        self.informationQueue = queue.Queue()
        
        self.resultList = [] # list of lists to store the results from each api
        self.threads = [] # list of threads to store the threads for each api
        self.informationList = [] # list of lists to store infomation from the function objectify 
        self.sortedResults = [] # list of objects to store the sorted results
        self.emptyApiList = [] # list of stores that returned empty results

        self.storeList = set()

        self.requestedApiAmount = 0
        self.numberOfSorted = 0
        self.nubmerOfObjectified = 0
        self.emptyApi=0

        self.keyword=""
        self.sortType = ""
        self.error = ""

        self.sortAscending= None
        self.currencyType = "USD"


       
        
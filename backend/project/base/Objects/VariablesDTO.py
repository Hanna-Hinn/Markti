import queue

class VariablesDTO:
    def __init__(self,dataQueue=None,resultList=None,requestedApiAmount=None
                 ,informationList=None,informationQueue=None,sortedResults=None,
                 numberOfSorted=None,nubmerOfObjectified=None,keyword=None,storeList=None
                 ,threads=None,sortType=None,sortAscending=None,currencyType=None,error=None):
       

        self.dataQueue = queue.Queue()
        self.informationQueue = queue.Queue()
        
        self.resultList = []
        self.threads = []
        self.informationList = []
        self.sortedResults = []

        self.storeList = set()

        self.requestedApiAmount = 0
        self.numberOfSorted = 0
        self.nubmerOfObjectified = 0

        self.keyword=""
        self.sortType = ""
        self.error = False

        self.sortAscending= None
        self.currencyType = "USD"
        
       
        
import queue

class VariablesDTO:
    def __init__(self,dataQueue=None,resultList=None,requestedApiAmount=None,informationList=None,informationQueue=None,sortedResults=None,numberOfSorted=None,nubmerOfObjectified=None,keyword=None,storeList=None,threads=None):
        self.dataQueue = queue.Queue()
        self.resultList = []
        self.requestedApiAmount = 0
        
        self.informationList = []
        self.informationQueue = queue.Queue()
        self.sortedResults = []
        self.numberOfSorted = 0
        self.nubmerOfObjectified = 0
        self.keyword=""
        self.storeList = []
        self.threads = []
        
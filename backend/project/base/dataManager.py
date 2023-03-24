import threading 
from .watchDog import watchDog

StoreFilter = { "Amazon", "Ebay", "AliExpress", "RealTime", "Shein" }

class dataManager:
    MIN_MERGE = 32
   # define function called start_watchdog that takes a list and sends it to the watchDog class
    def start_watchdog(self, functions):
        self.watchdog = watchDog(functions)
        self.watchdog.watch_functions()

    def __init__(self):
        self.data_lock = threading.Lock()
        self.sorted_data = []
        self.sorting_in_progress = False
    
    def dog_finished(self):
        # when the watchdog is done it calls this function
        # this function sends back a flag true if finshed 
        # if not it returns false
        if self.sorting_in_progress:
            return False
        else:
            return True

        
    
        
    def data_SendToDataManager(self, data):
        with self.data_lock:
            self.sorted_data.append(data)
            if not self.sorting_in_progress:
                self.sort_data()
        
    def sort_data(self):
            self.sorting_in_progress = True
            data = self.sorted_data
            n = len(data)
            if n < self.MIN_MERGE:
                # Use insertion sort for small arrays
                for i in range(1, n):
                    key = data[i]
                    j = i - 1
                    while j >= 0 and data[j] > key:
                        data[j + 1] = data[j]
                        j -= 1
                    data[j + 1] = key
            else:
                # Use Tim Sort for larger arrays
                runs, sorted_data = [], []
                i = 0
                while i < n:
                    j = i + 1
                    while j < n and data[j] >= data[j - 1]:
                        j += 1
                    if j - i > 1:
                        runs.append(data[i:j])
                    else:
                        sorted_data.append(data[i])
                    i = j

                while len(runs) > 1:
                    runs.append(self.merge_runs(runs.pop(0), runs.pop(0)))

                sorted_data.extend(runs[0])

                self.sorted_data = sorted_data
            self.sorting_in_progress = False
            print("Sorted data:", sorted_data)

    def merge_runs(self, a, b):
        if not a or not b:
            return a or b

        if a[-1] <= b[0]:
            return a + b

        if b[-1] <= a[0]:
            return b + a

        result = []
        i, j = 0, 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        if i == len(a):
            result.extend(b[j:])
        else:
            result.extend(a[i:])

        return result
    def get_error(self):
        # return an error if there was a problem with the data processing
        pass # TODO: implement the error handling code
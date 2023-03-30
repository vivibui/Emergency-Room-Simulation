

class Queue: 
    def __init__(self): 
        self.__queue = []
    
    def enqueue(self, patient): 
        self.__queue.append(patient)

    def dequeue(self, patient): 
        self.__queue.remove(patient)

    def get_queue(self): 
        return self.__queue

  

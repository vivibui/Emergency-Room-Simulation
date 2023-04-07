

class Queue: 
    def __init__(self): 
        self.__queue = []
    
    def enqueue(self, patient): 
        self.__queue.append(patient)

    def dequeue(self, patient): 
        if self.__queue: 
            self.__queue.remove(patient)

    def push_to_end(self): 
        # Push a patient from the first in queue to the end of queue
        if self.__queue: 
            patient = self.__queue.pop(0)
            self.__queue.append(patient)
            return patient

    def get_queue(self): 
        return self.__queue

  

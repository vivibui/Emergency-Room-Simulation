

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
    
class Patient: 
    def __init__(self, num): 
        self.num = num 



def CreateProbe(all_waiting, i, p): 
    return all_waiting[i:(i+p)]
    

######## TESTING HERE ########

queue = Queue() 
queue.enqueue(Patient(1))
queue.enqueue(Patient(2))
queue.enqueue(Patient(3))
queue.enqueue(Patient(4))
queue.enqueue(Patient(5))
queue.enqueue(Patient(6))
queue.enqueue(Patient(7))
queue.enqueue(Patient(8))
queue.enqueue(Patient(9))
queue.enqueue(Patient(10))
queue.enqueue(Patient(11))

print(len(queue.get_queue()))

probes = 4
p = 2 
index = 0 
matrix = []
for i in range(probes): 
    probe = CreateProbe(queue.get_queue(), index, p)
    matrix.append(probe)
    index += p

print("CHECK MATRIX:", len(matrix))


r = len(queue.get_queue())%probes
i_matrix = 0 
for i in range(r): 
    matrix[i_matrix].append(queue.get_queue()[index])
    index += 1
    i_matrix += 1


count_probe = 0 
for i in matrix: 
    count_probe += 1 
    print(f'PROBE {count_probe}---------')
    for j in range(len(i)): 
        print(i[j].num)
    print() 


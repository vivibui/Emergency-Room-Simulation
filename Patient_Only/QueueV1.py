

import ConfigV1 as cf 

# This is where we (1) create queue and (2) select patient from queue 

def Queue(all_patients): 
    queue = []
    # Queue: list of patient objects  
    for patient in all_patients: 
        if patient.get_status() == 0: 
            # queue[int(patient.get_id())] = int(patient.get_priority_score())
            queue.append(patient)
    return queue


'''
#################################################################  
# METHOD 1: First come first serve
#################################################################
def SelectFromQueue(queue, emergency_room, day, time):
# Waiting ID: a list of ID from queue, sorted ascendingly 
    waiting_ID = [] 
    for patient in queue: 
        waiting_ID.append(patient.get_id())
    waiting_ID.sort() 
    get_person = emergency_room.get_patient(waiting_ID[0])
    return get_person 


#################################################################  
# METHOD 2: C1 - Rule stated below
################################################################# 

def SelectFromQueue(queue, day, time):
    # Initialize
    max_wait = 0 
    min_score = 10000 
    # Get patient to assign to bed 
        #### Before Benchmark W: Priority Score > FIFO 
        #### After Benchmark W: LIFO 
        # First, a person who has been waiting the longest 
            # and their wait time is more than BENCHMARK_W hour will be prioritized 
        # Second, base on priority score: the lower the higher the priority 
        # If multiple patients have the same min priority score, then base on order: 
            # the smaller the id the higher the priority 
    for patient in queue: 
        person_wait_time = patient.calc_wait_time(day, time) 
        person_priority_score = patient.get_priority_score() 
        if person_wait_time > max_wait: 
            max_wait = person_wait_time 
            max_patient = patient 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
    if max_wait >= cf.BENCHMARK_W: 
        return max_patient 
    else: 
        return min_patient 
    
'''
#################################################################  
# METHOD 3: C2 - Rule stated below
################################################################# 

def SelectFromQueue(queue, day, time):
    # Initialize
    max_wait = 0 
    min_score = 10000 
    # Get patient to assign to bed 
        #### Before Benchmark W: Priority Score > FIFO 
        #### After Benchmark W: LIFO 
        # First, base on priority score: the lower the higher the priority 
        # If the same min priority score, then base on order: the smaller the id the higher the priority 
        # If maximum wait time of a patient reached Benchmark W -> LIFO 
    for patient in queue: 
        person_wait_time = patient.calc_wait_time(day, time) 
        person_priority_score = patient.get_priority_score() 
        if person_wait_time > max_wait: 
            max_wait = person_wait_time 
            max_patient = patient 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
    if max_wait >= cf.BENCHMARK_W: 
        return patient # LIFO applied after when a queuing patient with max wait time reached benchmark W 
    else: 
        return min_patient 
  

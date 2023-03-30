
import ConfigV1 as cf 


'''
#################################################################  
# METHOD 1: First come first serve
#################################################################
def SelectFromQueue(queue, day, time):
    return queue.get_queue()[0]


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
    for patient in queue.get_queue(): 
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
    for patient in queue.get_queue(): 
        person_wait_time = patient.calc_wait_time(day, time) 
        person_priority_score = patient.get_priority_score() 
        if person_wait_time > max_wait: 
            max_wait = person_wait_time 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
    if max_wait >= cf.BENCHMARK_W: 
        return patient # LIFO applied after when a queuing patient with max wait time reached benchmark W 
    else: 
        return min_patient

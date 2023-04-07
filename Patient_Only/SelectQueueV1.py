
import ConfigV1 as cf 

FLAG = 1 

'''
#################################################################  
# METHOD 1: First come first serve
#################################################################
def SelectFromQueue(queue, day, time):
    return queue.get_queue()[0]
''' 

''' 
#################################################################  
# METHOD 2: C1 
################################################################# 

# Get patient to assign to bed 
        #### Before Benchmark W: Priority Score > FIFO 
        #### After Benchmark W: FIFO 
        # First, a person who has been waiting the longest 
            # and their wait time is more than BENCHMARK_W hour will be prioritized 
        # Second, base on priority score: the lower the higher the priority 
        # If multiple patients have the same min priority score, then base on order: 
            # the smaller the id the higher the priority 

def SelectFromQueue(queue, day, time):
    # Initialize
    min_score = 10000 

    all_waiting = queue.get_queue()

    if len(all_waiting) == 1: 
        return all_waiting[0]
    
    for patient in all_waiting: 
        person_priority_score = patient.get_priority_score() 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
    if all_waiting[0].calc_wait_time(day, time) >= cf.BENCHMARK_W: 
        return all_waiting[0]
    else: 
        return min_patient 
'''   

''' 
#################################################################  
# METHOD 3: C2 
################################################################# 

# Get patient to assign to bed 
        #### Before Benchmark W: Priority Score > FIFO 
        #### After Benchmark W: LIFO 
        # First, base on priority score: the lower the higher the priority 
        # If the same min priority score, then base on order: the smaller the id the higher the priority 
        # If maximum wait time of a patient reached Benchmark W -> LIFO 

def SelectFromQueue(queue, day, time):
    # Initialize
    min_score = 10000 
    
    all_waiting = queue.get_queue()

    if len(all_waiting) == 1: 
        return all_waiting[0]
    
    for patient in all_waiting: 
        person_priority_score = patient.get_priority_score() 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
    if all_waiting[0].calc_wait_time(day, time) >= cf.BENCHMARK_W: 
        return all_waiting[-1] # LIFO apply when the patient with the longest wait time hits Benchmark W 
    else: 
        return min_patient 
''' 

''' 
#################################################################  
# METHOD 4-1: A1-PP - Alternate (Priority)
################################################################# 

# Get patient to assign to bed 
        #### Before Benchmark W: Based on Priority Score 
        #### After Benchmark W: Alternate min and max Priority Score
        # First, base on priority score: the lower the higher the priority 
        # If multiple patients have the same min priority score, then base on order: 
            # the smaller the id the higher the priority 
        # If the wait time of first patient in queue passes Bechnmark W: 
            # Alternate between selecting the max and min priority score 
            # If multiple patients have the same min or max score, thenn base on the order

def SelectFromQueue(queue, day, time):
    # Initialize
    min_score = 10000 
    max_score = 0 
    
    all_waiting = queue.get_queue()

    if len(all_waiting) == 1: 
        return all_waiting[0]

    for patient in all_waiting: 
        person_priority_score = patient.get_priority_score() 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
        if person_priority_score > max_score: 
            max_score = person_priority_score
            max_patient = patient 
    
    if all_waiting[0].calc_wait_time(day, time) >= cf.BENCHMARK_W:
        global FLAG
        if FLAG == 1: 
            FLAG = 2
            return min_patient
        else: 
            FLAG = 1
            return max_patient
    else: 
        return min_patient 
''' 

#################################################################  
# METHOD 4-2: A2-PQ - Alternate (FIFO and LIFO)
################################################################# 

# Get patient to assign to bed 
        #### Before Benchmark W: Based on Priority Score 
        #### After Benchmark W: Alternate min and max Priority Score
        # First, base on priority score: the lower the higher the priority 
        # If multiple patients have the same min priority score, then base on order: 
            # the smaller the id the higher the priority 
        # If the wait time of first patient in queue passes Bechnmark W: 
            # Alternate between selecting the patient with the most and the least wait time

def SelectFromQueue(queue, day, time):
    # Initialize
    min_score = 10000 
    
    all_waiting = queue.get_queue()

    if len(all_waiting) == 1: 
        return all_waiting[0]

    for patient in all_waiting: 
        person_priority_score = patient.get_priority_score() 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
    
    if all_waiting[0].calc_wait_time(day, time) >= cf.BENCHMARK_W:
        global FLAG
        if FLAG == 1: 
            FLAG = 2
            return all_waiting[0]
        else: 
            FLAG = 1
            return all_waiting[-1]
    else: 
        return min_patient 

''' 
#################################################################  
# METHOD 5: Z1-PQ - Alternate with Two Probes 
################################################################# 

# Get patient to assign to bed 
        #### Before Benchmark W: Based on Priority Score 
        #### After Benchmark W: Alternate FIFO in probe
        # First, base on priority score: the lower the higher the priority 
        # If multiple patients have the same min priority score, then base on order: 
            # the smaller the id the higher the priority 
        # If the wait time of first patient in queue passes Bechnmark W: 
            # Divide the queue into half 
            # Alternate between selecting patient first-in-line in probe 1 and probe 2 

def SelectFromQueue(queue, day, time):
    # Initialize
    min_score = 10000 
    
    all_waiting = queue.get_queue()

    if len(all_waiting) == 1: 
        return all_waiting[0]

    for patient in all_waiting: 
        person_priority_score = patient.get_priority_score() 
        if person_priority_score < min_score: 
            min_score = person_priority_score
            min_patient = patient 
    
    if all_waiting[0].calc_wait_time(day, time) >= cf.BENCHMARK_W:
        if len(all_waiting)%2 == 0: 
            x = len(all_waiting)//2
        else: 
            # If the number of patients in queue is odd 
                # probe 2 will larger than probe 1 by one patient
                # since probe 2 stores the last patient 
            x = (len(all_waiting)-1)//2
        probe1 = all_waiting[:x]
        probe2 = all_waiting[x:] 
        global FLAG
        if FLAG == 1: 
            FLAG = 2
            return probe2[0]
        else: 
            FLAG = 1
            return probe1[0]
    else: 
        return min_patient 

''' 

#################################################################  
# METHOD 6-1: Z2-PQ - Alternate with Multiple Probes 
################################################################# 

# Get patient to assign to bed 
        #### Before Benchmark W: Based on Priority Score 
        #### After Benchmark W: Alternate 
        # First, base on priority score: the lower the higher the priority 
        # If multiple patients have the same min priority score, then base on order: 
            # the smaller the id the higher the priority 
        # If the wait time of first patient in queue passes Bechnmark W: 
            # Divide the queue into the number of probes 
            # Alternate between selecting the first-in-line in each probe 


#################################################################  
# METHOD 6-2: Z3-Q - Alternate FIFO with Multiple Probes (remove Benchmark W)  
################################################################# 

# Get patient to assign to bed 
        # Divide the queue into the number of probes 
        # Alternate between selecting the first-in-line in each probe 
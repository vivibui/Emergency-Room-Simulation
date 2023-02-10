

import ConfigV2 as cf 

# This is where we (1) create queue and (2) select patient from queue 


def AddQueue(all_patients): 
    queue = {} 
    # Queue: a dictionary of ID:priority score of waiting patients 
    for patient in all_patients: 
        if patient.get_status() == 0: 
            queue[int(patient.get_id())] = int(patient.get_priority_score())
    return queue



def SelectFromQueue(queue, emergency_room, day, time):
    # Waiting ID: a list of ID from queue, sorted ascendingly 
    waiting_ID = list(queue.keys()) 
    waiting_ID.sort() 
    # Initialize
    max_wait = 0 
    max_id = 0 
    # Get patient to assign to bed 
        # First, a person who has been waiting more than BENCHMARK hour will be prioritized 
        # Second, base on priority score: the lower the higher the priority 
        # Third, base on order: the smaller the id the higher the priority 
    for id in waiting_ID: 
        person = emergency_room.get_patient(id) 
        person_wait_time = person.calc_wait_time(day, time) 
        if person_wait_time > max_wait: 
            max_wait = person_wait_time 
            max_id = id 
    if max_wait >= cf.BENCHMARK_W: 
        get_person = emergency_room.get_patient(max_id) 
    else: 
        min_score = min(queue.values())
        id_to_select = [id for id in queue if queue[id] == min_score]
        id_to_select.sort() 
        get_person = emergency_room.get_patient(id_to_select[0])
    return get_person   

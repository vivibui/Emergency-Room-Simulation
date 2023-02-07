#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Queue                      ## 
##        Last updated: 02/07/2022         ##
##                                         ##
#############################################


# This is where we (1) create queue and (2) select patient from queue 


def CreateQueue(all_patients): 
    # Queue: a dictionary of ID:priority score of waiting patients 
    queue = {}  
    for patient in all_patients: 
        if patient.get_status() == 0: 
            queue[patient.get_id()] = patient.get_priority_score() 
    return queue



def SelectFromQueue(queue, emergency_room):
    # Waiting ID: a list of ID from queue, sorted ascendingly 
    waiting_ID = list(queue.keys()) 
    waiting_ID.sort() 
    # Get patient to assign to bed 
        # First, base on priority score: the lower the higher the priority 
        # Second, base on order: the smaller the id the higher the priority 
        # Third, base on rounds: a person cannot be skipped for more than 2 rounds regardless of priority score      
    # Third condition: 
    if len(waiting_ID) >= 2: 
        if waiting_ID[1] - waiting_ID[0] >= 2: 
            get_person = emergency_room.get_patient(waiting_ID[0])
        else: 
            # First condition and second condition:  
            min_score = min(queue.values())
            id_to_select = [id for id in queue if queue[id] == min_score]
            id_to_select.sort() 
            get_person = emergency_room.get_patient(id_to_select[0])
    else: # only one patient waiting
        get_person = emergency_room.get_patient(waiting_ID[0])
    return get_person   
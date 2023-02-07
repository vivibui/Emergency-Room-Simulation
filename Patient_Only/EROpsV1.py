#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: ER Operation               ## 
##        Last updated: 02/07/2022         ##
##                                         ##
#############################################

import PatientOpsV1 as po 

def ReleasePatient(emergency_room, all_patients, time): 
    count_release = 0 
    # Loop to release patients from beds 
    for patient in all_patients: 
        if patient.get_status() == 1:
        # Deduct time staying in ER per treating patient
            patient.deduct_time_in_ER() 
            if patient.get_time_in_ER() == 0: 
            # Change status from Treating to Treated 
                patient.set_status(2)
                # Update day released
                patient.set_time_released(time)
                # Release a bed 
                emergency_room.bed_release()
                count_release +=1
    return emergency_room, count_release 



def CreateQueue(all_patients): 
    # Queue: a dictionary of ID:priority score of waiting patients 
    queue = {}  
    for patient in all_patients: 
        if patient.get_status() == 0: 
            queue[patient.get_id()] = patient.get_priority_score() 
    return queue



def SelectFromQueue(waiting_ID, queue, emergency_room):
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



def AssignBed(queue, emergency_room, time): 
    # Waiting ID: a list of ID from queue, sorted ascendingly 
    waiting_ID = list(queue.keys()) 
    waiting_ID.sort() 
    # Bed is taken 
    emergency_room.bed_taken()
    # Select a person from queue 
    get_person = SelectFromQueue(waiting_ID, queue, emergency_room)        
    # Change status from Waiting to Treating 
    get_person.set_status(1)
    # Set time stay in ER
    po.TimeInER(get_person)
    # Set day admitted 
    get_person.set_time_admitted(time)
    # Remove selected patient from queue and waiting ID 
    del queue[get_person.get_id()]

    return emergency_room, queue 
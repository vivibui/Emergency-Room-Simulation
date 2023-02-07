#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: ER Operation               ## 
##        Last updated: 02/07/2022         ##
##                                         ##
#############################################

import PatientOpsV1 as po 
import QueueV1 as qu 

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


def AssignBed(queue, emergency_room, time): 
    # Bed is taken 
    emergency_room.bed_taken()
    # Select a person from queue 
    get_person = qu.SelectFromQueue(queue, emergency_room)        
    # Change status from Waiting to Treating 
    get_person.set_status(1)
    # Set time stay in ER
    po.TimeInER(get_person)
    # Set day admitted 
    get_person.set_time_admitted(time)
    # Remove selected patient from queue and waiting ID 
    del queue[get_person.get_id()]

    return emergency_room, queue 
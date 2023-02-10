#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Simulation of One Day      ## 
##                                         ##
#############################################


import random 
import EmergencyRoomV1
import AuxiliaryV1 as aux 
import PatientOpsV1 as po 
import EROpsV1 as eo 
import QueueV1 as qu
import PrintingV1 as prt



def OneDaySimulation(day, p_id, emergency_room, content_ops, MAX_PATIENTS): 
    # Initialize 
    count_release = 0 

    # Create new patient and add to list
    total_patient_today = random.randint(0,MAX_PATIENTS)
    all_patients = emergency_room.get_patients()
    for i in range(total_patient_today): 
        p_id = aux.IDIncrement(p_id) 
        # Pass list of new patients today to the Emergency Room 
        all_patients.append(po.NewPatient(p_id, day)) 
        
    # Release patients from beds 
    emergency_room, count_release = eo.ReleasePatient(emergency_room, all_patients, day)

    # Loop to arrange patients to available beds 
    while emergency_room.get_open_beds() > 0 and emergency_room.count_waiting() > 0: 
        # Create queue 
        queue = qu.CreateQueue(all_patients)
        # Times assigning beds for today 
        if emergency_room.get_open_beds() > emergency_room.count_waiting(): 
            time_assign_beds = emergency_room.count_waiting() 
        else: 
            time_assign_beds = emergency_room.get_open_beds() 
        # Assign beds to waiting patients 
        for i in range(time_assign_beds):
            emergency_room, queue = eo.AssignBed(queue, emergency_room, day)

    # Print Output 
    output = prt.Output(emergency_room, total_patient_today, day, count_release)

    # To write Emergency Operations to csv
    content_ops += output + "\n"

    return emergency_room, content_ops, p_id 
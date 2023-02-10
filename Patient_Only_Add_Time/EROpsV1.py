

import PatientOpsV1 as po 
import QueueV1 as qu 
import Satisfaction as sf 

def ReleasePatient(emergency_room, all_patients, day, time, count_release): 
    # Loop to release patients from beds 
    for patient in all_patients: 
        if patient.get_status() == 1:
        # Deduct time staying in ER per treating patient
            patient.deduct_time_in_ER() 
            if patient.get_length_stay_in_ER() <= 0: 
            # Change status from Treating to Treated 
                patient.set_status(2)
                # Update day and time released
                patient.set_time_released(time)
                patient.set_day_released(day)
                # Release a bed 
                emergency_room.bed_release()
                count_release +=1
    return emergency_room, count_release 
    

def AssignBed(queue, emergency_room, day, time): 
    # Bed is taken 
    emergency_room.bed_taken()
    # Select a person from queue 
    get_person = qu.SelectFromQueue(queue, emergency_room, day, time)        
    # Change status from Waiting to Treating 
    get_person.set_status(1)
    # Set time stay in ER
    po.TimeInER(get_person)
    # Set day and time admitted 
    get_person.set_time_admitted(time)
    get_person.set_day_admitted(day)
    # Set total wait time 
    total_wait_time = get_person.calc_wait_time(day, time)
    get_person.set_total_wait_time(int(total_wait_time))
    # Calculate satisfaction score 
    score = sf.CalSatisfaction(get_person)
    get_person.set_satisfaction_score(score) 
    # Remove selected patient from queue and waiting ID 
    del queue[get_person.get_id()]

    return emergency_room, queue 

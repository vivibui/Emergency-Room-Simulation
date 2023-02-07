#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ##
##        Last updated: 12/26/2022         ##
##                                         ##
#############################################



import random 
import EmergencyRoomV2
import PatientV2
import StaffV2 


# Max days to run simulation 
MAX_DAYS = 20
# Max patients coming in a day  
MAX_PATIENTS = 5
# Initial Condition: ER Capacity 
MAX_BEDS = 50
AVAIL_BEDS = 5



def PriorityScore(patient): 
    # Priority order: Acute level -> Age 
    # The lower the score, the higher priority the patient is 

    # Acute Level
    score = 0
    score += patient.get_acute_level()
    # Age group Priority 
    if patient.get_age() <= 10 or patient.get_age() >= 65: 
        score += 0.1
    elif patient.get_age() > 10 and patient.get_age() < 21: 
        score += 0.2 
    else: 
        score += 0.3
    return score 



def NewPatient(p_id, t): 
    p_age = random.randint(1,105) # Max age is 105 
    p_acute_level = random.randint(1,5)
    p_pain_level = random.randint(1,10)
    p_code = "P"
    p_time_coming = t
    p_new_patient = PatientV2.Patient(code = p_code, id = p_id, age = p_age, acute_level = p_acute_level, pain_level = p_pain_level, time_coming = p_time_coming)
    p_priority_score = PriorityScore(p_new_patient)
    p_new_patient.set_priority_score(p_priority_score)
    return p_new_patient 



def TimeInER(person): 
    # Set time stay in ER based on pain level
    if person.get_acute_level() == 1: 
        mean_time = 5
    elif person.get_acute_level() == 2: 
        mean_time = 4
    elif person.get_acute_level() == 3: 
        mean_time = 3
    elif person.get_acute_level() == 4: 
        mean_time = 2
    else: 
        mean_time = 1 
    # Set ER time 
    person.set_time_in_ER(mean_time)


def write_to_txt(file_name, header, content): 
    write_file = open(file_name, "w")
    write_file.write(header) 
    write_file.write(content) 
    write_file.close() 

def main(): 
    
    # Initialize 
    day = 0 
    id = 0
    count_release = 0 
    emergency_room = EmergencyRoomV2.EmergencyRoom(total_beds = MAX_BEDS, open_beds = AVAIL_BEDS)
    content_ops = ""  # to export result 
    content_patients = "" # to export result 


    # Initial Information
    print()
    print("Total number of beds:", MAX_BEDS)
    print("Beds available first opening:", emergency_room.get_open_beds()) 
        
    # Output Header
    print()
    header = format("Day", "5s") + format("New Patients", "18s") + format("Available Beds", "18s") + format("Waiting", "12s") \
             + format("Treating", "12s") + format("Treated", "12s") + format("Beds Released", "18s") + "\n"
    print() 
    print(header)

    # Loop day 
    while day < MAX_DAYS: 
        day += 1 

        # Create new patient and add to list
        total_patient_today = random.randint(0,MAX_PATIENTS)
        all_patients = emergency_room.get_patients()
        for i in range(total_patient_today): 
            id += 1 
            # Pass list of new patients today to the Emergency Room 
            all_patients.append(NewPatient(id, day)) 
            
        # Loop to release patients from beds 
        for patient in all_patients: 
            if patient.get_status() == 1:
                # Deduct time staying in ER per treating patient
                patient.deduct_time_in_ER() 
                if patient.get_time_in_ER() == 0: 
                    # Change status from Treating to Treated 
                    patient.set_status(2)
                    # Update day released
                    patient.set_time_released(day)
                    # Release a bed 
                    emergency_room.bed_release()
                    count_release +=1

        # Loop to arrange patients to available beds 
        while emergency_room.get_open_beds() > 0 and emergency_room.count_waiting() > 0: 

            # Queue: a dictionary of ID:priority score of waiting patients 
            queue = {}  
            for patient in all_patients: 
                if patient.get_status() == 0: 
                    queue[patient.get_id()] = patient.get_priority_score() 
            waiting_ID = list(queue.keys()) 
            waiting_ID.sort()
            
            # Times assigning beds for today 
            if emergency_room.get_open_beds() > emergency_room.count_waiting(): 
                time_assign_beds = emergency_room.count_waiting() 
            else: 
                time_assign_beds = emergency_room.get_open_beds() 


            # ********************* ASSIGNING BEDS *********************

            for i in range(time_assign_beds):
                
                #--------------- Emergency room --------------- 
                # Bed is taken 
                emergency_room.bed_taken()

                #--------------- Patient --------------- 
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
                
                # Change status from Waiting to Treating 
                get_person.set_status(1)

                # Set time stay in ER
                TimeInER(get_person)

                # Set day admitted 
                get_person.set_time_admitted(day)

                # Remove selected patient from queue and waiting ID 
                del queue[get_person.get_id()]
                waiting_ID = list(queue.keys()) 
                waiting_ID.sort() 

        # Print Output 
        output = format(day, "<5d") + format(total_patient_today, "<18d") + format(emergency_room.get_open_beds(), "<18d") \
                 + format(emergency_room.count_waiting(), "<12d") + format(emergency_room.count_treating(), "<12d") \
                 + format(emergency_room.count_treated(), "<12d") + format(count_release, "<18d")
        print(output)

        # Reset 
        count_release = 0

        # To write Emergency Operations to csv: 
        content_ops += output + "\n"
        
    # Print Patients
    print() 
    print()
    print("----------------------------------- LIST OF PATIENTS ----------------------------------- ")
    print()
    print() 
    header_patients = format("Day Come In", "15s") + format("ID", "10s") + format("Age", "10s") \
            + format("Acute Level", "20s") + format("Pain Level", "20s") \
                + format("Status", "10s") + format("Day Admitted", "20s") + format("Day Released", "20s")
    print(header_patients)
    print()
    for patient in emergency_room.get_patients(): 
        print(patient.__str__())
        # To write list of patients to csv: 
        content_patients += patient.__str__() + "\n"
    print()

    # Write to txt 
    write_to_txt("emergency_ops", header, content_ops)
    write_to_txt("patients_list", header_patients, content_patients)

main()

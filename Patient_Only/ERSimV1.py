#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ##
##        Last updated: 02/03/2022         ##
##                                         ##
#############################################



import random 
import EmergencyRoomV1
import PatientOpsV1 as po 
import EROpsV1 as eo 

# Max days to run simulation 
MAX_DAYS = 20
# Max patients coming in a day  
MAX_PATIENTS = 5
# Initial Condition: ER Capacity 
MAX_BEDS = 50
AVAIL_BEDS = 5


def write_to_txt(file_name, header, content): 
    write_file = open(file_name, "w")
    write_file.write(header) 
    write_file.write(content) 
    write_file.close() 


def main(): 
    
    # Initialize 
    day = 0 
    count_release = 0 
    id = 0 
    emergency_room = EmergencyRoomV1.EmergencyRoom(total_beds = MAX_BEDS, open_beds = AVAIL_BEDS)
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
            all_patients.append(po.NewPatient(id, day)) 
        

        # Release patients from beds 
        emergency_room, count_release = eo.ReleasePatient(emergency_room, all_patients, day)


        # Loop to arrange patients to available beds 
        while emergency_room.get_open_beds() > 0 and emergency_room.count_waiting() > 0: 

            queue = eo.CreateQueue(all_patients)
            
            # Times assigning beds for today 
            if emergency_room.get_open_beds() > emergency_room.count_waiting(): 
                time_assign_beds = emergency_room.count_waiting() 
            else: 
                time_assign_beds = emergency_room.get_open_beds() 


            # ********************* ASSIGNING BEDS *********************

            for i in range(time_assign_beds):
                emergency_room, queue = eo.AssignBed(queue, emergency_room, day)


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


if __name__ == '__main__':
    main() 

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
import PrintingV1 as prt
import AuxiliaryV1 as aux 
import QueueV1 as qu

# Max days to run simulation 
MAX_DAYS = 20
# Max patients coming in an hour  
MAX_PATIENTS = 5
# Initial Condition: ER Capacity 
AVAIL_BEDS = 5


def main(): 
    
    # Initialize 
    day = 0 
    count_release = 0 
    p_id = 0 
    emergency_room = EmergencyRoomV1.EmergencyRoom(open_beds = AVAIL_BEDS)
    content_ops = ""  # to export result 

    # Print Header 
    header = prt.Header(AVAIL_BEDS)

    # Loop day 
    while day < MAX_DAYS: 
        day += 1 
        
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

        # Reset 
        count_release = 0

        # To write Emergency Operations to csv
        content_ops += output + "\n"
        
    # Print Patients
    header_patients, content_patients = prt.ListPatients(emergency_room) 

    # Write to csv
    aux.ExportCSV("emergency_ops", header, content_ops)
    aux.ExportCSV("patients_list", header_patients, content_patients)


if __name__ == '__main__':
    main() 

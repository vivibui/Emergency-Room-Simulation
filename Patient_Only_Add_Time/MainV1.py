#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ##
##                                         ##
#############################################

import random 
import datetime 
import EmergencyRoomV1 
import AuxiliaryV1 as aux 
import PatientOpsV1 as po 
import EROpsV1 as eo 
import QueueV1 as qu
import PrintingV1 as prt


# Max days to run simulation 
MAX_DAYS = 3
# Max patients coming in an hour  
MAX_PATIENTS = 5
# Initial Condition: ER Capacity 
AVAIL_BEDS = 15


def main(): 
    
    # Initialize 
    day = 0 
    p_id = 0 
    emergency_room = EmergencyRoomV1.EmergencyRoom(open_beds = AVAIL_BEDS)
    content_ops = ""  # to export result 

    # Print Header 
    header = prt.Header(AVAIL_BEDS)

    # Loop day 
    while day < MAX_DAYS: 
        day += 1 
        h = 0 

        for h in range(24): 
            # Initialize 
            total_patients_one_hour = random.randint(0,MAX_PATIENTS)
            all_patients = emergency_room.get_patients()
            minutes_list = [ random.randint(0,60) for i in range(total_patients_one_hour) ]

            for m in range(60): 
                time = datetime.time(hour = h, minute = m) 
                # New patients 
                if m in minutes_list: 
                    p_id = aux.IDIncrement(p_id) 
                    # Pass list of new patients today to the Emergency Room 
                    all_patients.append(po.NewPatient(p_id, day, time)) 
               
                # Release patient 
                emergency_room, count_release = eo.ReleasePatient(emergency_room, all_patients, day, time)

                # Loop to arrange patients to available beds 
                while emergency_room.get_open_beds() > 0 and emergency_room.count_waiting() > 0: 
                    # Create queue 
                    queue = qu.CreateQueue(all_patients)
                    # Number of times assigning beds
                    if emergency_room.get_open_beds() > emergency_room.count_waiting(): 
                        times_assign_beds = emergency_room.count_waiting() 
                    else: 
                        times_assign_beds = emergency_room.get_open_beds() 
                    # Assign beds to waiting patients 
                    for i in range(times_assign_beds):
                        emergency_room, queue = eo.AssignBed(queue, emergency_room, day, time)


        # Print Output 
        # output = prt.Output(emergency_room, total_patients_per_day, day, count_release)

        # To write Emergency Operations to csv
        # content_ops += output + "\n"

        # emergency_room, content_ops, p_id = sim.OneDaySimulation(day, p_id, emergency_room, content_ops, MAX_PATIENTS) 

    # Print Patients
    header_patients, content_patients = prt.ListPatients(emergency_room) 

    # Write to csv
    # aux.ExportCSV("emergency_ops", header, content_ops)
    aux.ExportCSV("patients_list", header_patients, content_patients)



if __name__ == '__main__':
    main() 

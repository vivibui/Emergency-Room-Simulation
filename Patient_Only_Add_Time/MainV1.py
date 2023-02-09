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
import ConfigV1 as cf 


def main(): 
    
    # Initialize 
    day = 0 
    p_id = 0 
    emergency_room = EmergencyRoomV1.EmergencyRoom(open_beds = cf.AVAIL_BEDS)
    content_ops = ""  # to export result 

    # Loop day 
    while day < cf.MAX_DAYS: 
        day += 1 
        h = 0 
        # Print Header 
        header = prt.LogHeader(day)
        content_ops += header 

        for h in range(24): 
            # Initialize 
            total_patients_one_hour = random.randint(0,cf.MAX_PATIENTS)
            all_patients = emergency_room.get_patients()
            minutes_list = [ random.randint(0,60) for i in range(total_patients_one_hour) ]
            count_release = 0

            for m in range(60): 
                time = datetime.time(hour = h, minute = m) 
                # New patients 
                if m in minutes_list: 
                    p_id = aux.IDIncrement(p_id) 
                    # Pass list of new patients today to the Emergency Room 
                    all_patients.append(po.NewPatient(p_id, day, time)) 
               
                # Release patient 
                emergency_room, count_release = eo.ReleasePatient(emergency_room, all_patients, day, time, count_release)

                # Loop to arrange patients to available beds 
                while emergency_room.get_open_beds() > 0 and emergency_room.count_waiting() > 0: 
                    # Add to queue 
                    queue = qu.AddQueue(emergency_room)
                    # Number of times assigning beds
                    if emergency_room.get_open_beds() > emergency_room.count_waiting(): 
                        times_assign_beds = emergency_room.count_waiting() 
                    else: 
                        times_assign_beds = emergency_room.get_open_beds() 
                    # Assign beds to waiting patients 
                    for i in range(times_assign_beds):
                        emergency_room, queue = eo.AssignBed(queue, emergency_room, day, time)

            # Print Output 
            output = prt.LogOutput(emergency_room, total_patients_one_hour, h, count_release)

            # To write Emergency Operations to csv
            content_ops += output + "\n"

    # Print Patients
    header_patients, content_patients = prt.ListPatients(emergency_room) 

    # Write to csv
    aux.ExportCSV("emergency_ops", content_ops)
    aux.ExportCSV("patients_list", content_patients, header_patients)



if __name__ == '__main__':
    main() 

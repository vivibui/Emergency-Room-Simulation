
import sys
import random 
import datetime 

import EmergencyRoomV1 
import AuxiliaryV1 as aux 
import PatientOpsV1 as po 
import EROpsV1 as eo 
import QueueV1 as qu
import PrintingV1 as prt
import ConfigV1 as cf 


def main(n_seed): 
    
    # Initialize 
    day = 0 
    p_id = 0 
    emergency_room = EmergencyRoomV1.EmergencyRoom(open_beds = cf.AVAIL_BEDS)
    content_ER = ""  # to export result 

    # Loop day 
    while day < cf.MAX_DAYS: 
        day += 1 
        h = 0 
        # Print Header 
        header_ER = prt.LogHeader(day)

        for h in range(24): 
            # Initialize 
            total_patients_one_hour = random.randint(0,cf.MAX_PATIENTS)
            all_patients = emergency_room.get_patients()
            minutes_list = [ random.randint(0,60) for i in range(total_patients_one_hour) ]
            count_discharged = 0

            for m in range(60): 
                time = datetime.time(hour = h, minute = m) 
                # New patients 
                if m in minutes_list: 
                    p_id = aux.IDIncrement(p_id) 
                    # Pass list of new patients today to the Emergency Room 
                    all_patients.append(po.NewPatient(p_id, day, time)) 
               
                # Discharge patient 
                emergency_room, count_discharged = eo.ReleasePatient(emergency_room, all_patients, day, time, count_discharged)

                # Patients LWBS 
                eo.LWBS(all_patients, day, time)

                # Loop to arrange patients to available beds 
                while emergency_room.get_open_beds() > 0 and emergency_room.count_waiting() > 0: 
                    # Add to queue 
                    queue = qu.Queue(all_patients)
                    # Number of times assigning beds
                    if emergency_room.get_open_beds() > emergency_room.count_waiting(): 
                        times_assign_beds = emergency_room.count_waiting() 
                    else: 
                        times_assign_beds = emergency_room.get_open_beds() 
                    # Assign beds to waiting patients 
                    for i in range(times_assign_beds):
                        emergency_room, queue = eo.AssignBed(queue, emergency_room, day, time)

            # Print Output 
            output = prt.LogOutput(emergency_room, total_patients_one_hour, h, count_discharged, day)

            # To write Emergency Operations to csv
            content_ER += format(n_seed, "<30d") + output + "\n"

    # Print Patients
    header_patients, content_patients = prt.ListPatients(emergency_room, n_seed) 

    # Print Satisfaction Report 
    header_SF, content_SF = prt.ListSF(emergency_room, n_seed)

    # Add Sim Number to Headers
    header_ER, header_patients, header_SF = prt.AddSimHeader(header_ER), prt.AddSimHeader(header_patients), \
                                            prt.AddSimHeader(header_SF)

    # Write to csv
    aux.ExportCSV("emergency_ops_" + str(n_seed), content_ER, 1, header_ER)
    aux.ExportCSV("patients_list_" + str(n_seed), content_patients, 2, header_patients)
    aux.ExportCSV("satisfaction_report_" + str(n_seed), content_SF, 3, header_SF) 



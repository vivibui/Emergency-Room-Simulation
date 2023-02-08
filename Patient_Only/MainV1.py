#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ##
##                                         ##
#############################################


import EmergencyRoomV1
import AuxiliaryV1 as aux 
import PrintingV1 as prt
import OneSimV1 as sim  


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
        emergency_room, content_ops, p_id = sim.OneDaySimulation(day, p_id, emergency_room, content_ops, MAX_PATIENTS) 

    # Print Patients
    header_patients, content_patients = prt.ListPatients(emergency_room) 

    # Write to csv
    aux.ExportCSV("emergency_ops", header, content_ops)
    aux.ExportCSV("patients_list", header_patients, content_patients)



if __name__ == '__main__':
    main() 

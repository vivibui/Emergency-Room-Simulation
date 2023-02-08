#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Printing                   ## 
##                                         ##
#############################################



def Header(AVAIL_BEDS): 
    # Initial Information
    print()
    print("Beds available first opening:", AVAIL_BEDS) 
    # Header 
    print()
    header = format("Day", "5s") + format("New_Patients", "18s") + format("Available_Beds", "18s") + format("Waiting", "12s") \
             + format("Treating", "12s") + format("Treated", "12s") + format("Beds_Released", "18s") + "\n"
    print(header)
    print() 
    return header 


def BedAssignmentLog(): 
    print() 
    print('----------------------------------------')
    print("---------- BED ASSIGNMENT LOG ----------")
    print('----------------------------------------')
    header = format("Day", "5s") + format("Time", "18s") + format("Patient_ID", "5s") + "\n"

    
def Output(emergency_room, total_patient_today, time, count_release): 
    output = format(time, "<5d") + format(total_patient_today, "<18d") + format(emergency_room.get_open_beds(), "<18d") \
                 + format(emergency_room.count_waiting(), "<12d") + format(emergency_room.count_treating(), "<12d") \
                 + format(emergency_room.count_treated(), "<12d") + format(count_release, "<18d")
    print(output)
    return output 


def ListPatients(emergency_room): 
    content_patients = "" # to export result 
    print() 
    print()
    print("----------------------------------- LIST OF PATIENTS ----------------------------------- ")
    print()
    print() 
    header_patients =  format("ID", "10s") + format("Day_C", "10s") + format("Time_C", "20s") + \
                format("Age", "10s") + format("AcuteLv", "10s") + format("PainLv", "10s") \
                + format("Status", "10s") + format("Day_A", "10s") + format("Time_A", "20s") \
                    + format("Day_R", "10s") + format("Time_R", "20s")
    print(header_patients)
    print()
    for patient in emergency_room.get_patients(): 
        print(patient.__str__())
        # To write list of patients to csv: 
        content_patients += patient.__str__() + "\n"
    print()
    return header_patients, content_patients 
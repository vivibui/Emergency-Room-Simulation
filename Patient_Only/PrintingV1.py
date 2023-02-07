#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Printing                   ## 
##        Last updated: 02/07/2022         ##
##                                         ##
#############################################



def Header(AVAIL_BEDS): 
    # Initial Information
    print()
    print("Beds available first opening:", AVAIL_BEDS) 
    # Header 
    print()
    header = format("Day", "5s") + format("New Patients", "18s") + format("Available Beds", "18s") + format("Waiting", "12s") \
             + format("Treating", "12s") + format("Treated", "12s") + format("Beds Released", "18s") + "\n"
    print(header)
    print() 
    return header 


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
    return header_patients, content_patients 
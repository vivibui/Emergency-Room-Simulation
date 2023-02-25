

import ConfigV1 as cf 

def LogHeader(day): 
    print() 
    print('----------------------------------------')
    print(format(f'DAY {day}', "10s"))
    print('----------------------------------------')
    header = format(f'Day_{day}', '10s') + format("New_Patients", "20s") + format("Waiting", "15s") \
        + format("Assigned", "10s") + format("Discharged", "15s") + format("Beds_Avail_EOH", "15s") + "\n"
    print(header) 
    return header
    

def LogOutput(emergency_room, total_patient_today, h, count_discharged): 
    output = format(f'{h}:00', '<10s') + format(total_patient_today, '<20d') + format(emergency_room.count_waiting(), '<15d') \
        + format(emergency_room.count_treating(), '<10d') + format(count_discharged, '<15d') + format(emergency_room.get_open_beds(), "<15d")
    print(output)
    return output 


def ListPatients(emergency_room): 
    content_patients = "" # to export result 
    print() 
    print("--------------------------------------------------------------------------------------------------------")
    print("------------------------------------------- LIST OF PATIENTS -------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")
    print() 
    header_patients =  format("ID", "12s") + format("Day_C", "10s") + format("Time_C", "12s") \
                + format("Age", "10s") + format("AcuteLv", "10s") + format("PainLv", "10s") \
                + format("Priority", "10s") + format("Status", "10s") \
                    + format("Day_A", "10s") + format("Time_A", "12s") \
                    + format("Day_D", "10s") + format("Time_D", "12s") + format("Time_Left_In_ER", "20s") \
                        + format("Total_Wait_Time", "20s") + format("SF_Score", "15s") + "\n"
    print(header_patients)
    for patient in emergency_room.get_patients(): 
        print(patient.__str__())
        # To write list of patients to csv: 
        content_patients += patient.__str__() + "\n"
    return header_patients, content_patients 


def ListSF(emergency_room): 
    # Initialize 
    content_SF = ''
    total_patients_day = 0 
    total_SF_day = 0 
    # Print header 
    print() 
    print() 
    print('-------------------------------------------------')
    print('------ PATIENTS SATISFACTION SURVEY REPORT ------')
    print('-------------------------------------------------')
    # Loop to print 
    for day in range(1, cf.MAX_DAYS+1): 
        for patient in emergency_room.get_patients(): 
            if patient.get_day_coming() == day: 
                total_patients_day += 1 
                total_SF_day += patient.get_satisfaction_score() 
        avg_SF_day = round(total_SF_day/total_patients_day,2) 
        # Print 
        print(f'Day {day}: {avg_SF_day}') 
        content_SF += "Day " + str(day) + "| " + str(avg_SF_day) + "\n"
        # Reset 
        total_patients_day = 0 
        total_SF_day = 0 
    return content_SF 
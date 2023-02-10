

def LogHeader(day): 
    print() 
    print('----------------------------------------')
    print(format(f'DAY {day}', "10s"))
    print('----------------------------------------')
    header = format(f'Day_{day}', '10s') + format("New_Patients", "20s") + format("Waiting", "15s") \
        + format("Admitted", "10s") + format("Released", "10s") + format("Beds_Avail_EOH", "15s") + "\n"
    print(header) 
    return header
    

def LogOutput(emergency_room, total_patient_today, h, count_release): 
    output = format(f'{h}:00', '<10s') + format(total_patient_today, '<20d') + format(emergency_room.count_waiting(), '<15d') \
        + format(emergency_room.count_treating(), '<10d') + format(count_release, '<10d') + format(emergency_room.get_open_beds(), "<15d")
    print(output)
    return output 


def ListPatients(emergency_room): 
    content_patients = "" # to export result 
    print() 
    print("--------------------------------------------------------------------------------------------------------")
    print("------------------------------------------- LIST OF PATIENTS -------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------")
    print() 
    header_patients =  format("ID", "10s") + format("Day_C", "10s") + format("Time_C", "20s") + \
                format("Age", "10s") + format("AcuteLv", "10s") + format("PainLv", "10s") \
                + format("Status", "10s") + format("Day_A", "10s") + format("Time_A", "20s") \
                    + format("Day_R", "10s") + format("Time_R", "20s") + format("Time_Left_In_ER", "20s") + \
                        format("Total_Wait_Time", "20s") + "\n"
    print(header_patients)
    print()
    for patient in emergency_room.get_patients(): 
        print(patient.__str__())
        # To write list of patients to csv: 
        content_patients += patient.__str__() + "\n"
    print()
    return header_patients, content_patients 

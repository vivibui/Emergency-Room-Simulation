import os 

# Export file to CSV
def ExportCSV(file_name, content, folder_type, header=None): 
    dir = os.getcwd() 
    folder_path = os.path.join(dir,"Output")
    if folder_type == 1: 
        folder_path = os.path.join(folder_path,"EmergencyRoom")
    elif folder_type == 2: 
        folder_path = os.path.join(folder_path,"PatientList")
    else: 
        folder_path = os.path.join(folder_path,"Satisfaction")
    complete_name = os.path.join(folder_path, file_name)
    write_file = open(complete_name, "w")
    if header != None: 
        write_file.write(header) 
    write_file.write(content) 
    write_file.close() 

# Increment ID by 1 
def IDIncrement(id_type): 
    return id_type + 1 

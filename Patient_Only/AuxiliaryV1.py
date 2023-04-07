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

# Calculate default order of probes 
def CalProbeOrder(probes): 
    all_probes = []
    probes_order = []
    flag_probe = 0
    for i in range(probes):
        j = i + 1
        all_probes.append((j))
    while all_probes: 
        if flag_probe == 0: 
            probes_order.append(all_probes.pop(0))
            flag_probe = 1
        else: 
            probes_order.append(all_probes.pop(-1))
            flag_probe = 0 
    return probes_order

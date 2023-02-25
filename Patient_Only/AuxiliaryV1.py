import os 

# Export file to CSV
def ExportCSV(file_name, content, header=None): 
    dir = os.getcwd() 
    folder_path = os.path.join(dir,"Output")
    complete_name = os.path.join(folder_path, file_name)
    write_file = open(complete_name, "w")
    if header != None: 
        write_file.write(header) 
    write_file.write(content) 
    write_file.close() 

# Increment ID by 1 
def IDIncrement(id_type): 
    return id_type + 1 

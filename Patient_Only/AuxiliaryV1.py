

# Export file to CSV
def ExportCSV(file_name, content, header=None): 
    write_file = open(file_name, "w")
    if header != None: 
        write_file.write(header) 
    write_file.write(content) 
    write_file.close() 

# Increment ID by 1 
def IDIncrement(id_type): 
    return id_type + 1 

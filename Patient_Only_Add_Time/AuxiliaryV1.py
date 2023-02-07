#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Auxiliary Functions        ## 
##                                         ##
#############################################


# Export file to CSV
def ExportCSV(file_name, header, content): 
    write_file = open(file_name, "w")
    write_file.write(header) 
    write_file.write(content) 
    write_file.close() 

# Increment ID by 1 
def IDIncrement(id_type): 
    return id_type + 1 
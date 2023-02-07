#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Person Class               ## 
##        Last updated: 02/03/2022         ##
##                                         ##
#############################################

# ID is an integer 

class Person:
    def __init__(self, **kwargs): 
        self.__id = kwargs['id'] 
        

    ################################################   
    ###################  Get Method ################

    def get_id(self): 
        return self.__id 


    ################################################   
    #####################  Print ###################

    def __str__(self): 
        return format(self.__id, "<10d")

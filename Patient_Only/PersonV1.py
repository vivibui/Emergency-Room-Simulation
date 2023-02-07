#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Person Class               ## 
##        Last updated: 02/03/2022         ##
##                                         ##
#############################################

# ID is an integer 
# Code is a string 

class Person:
    def __init__(self, **kwargs): 
        self.__id = kwargs['id'] 
        self.__code = kwargs['code']
                

    ################################################   
    ###################  Get Method ################

    def get_id(self): 
        return self.__id 

    def get_code(self):
        return self.__code 


    ################################################   
    #####################  Print ###################

    def __str__(self): 
        return format(self.__id, "<10d")

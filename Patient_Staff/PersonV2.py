#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Patient Class              ## 
##        Last updated: 12/26/2022         ##
##                                         ##
#############################################

# Code for Patient starts with P 
# Code for Doctor starts with D
# Code for Specialist starts with S

class Person:
    def __init__(self, **kwargs): 
        self.__code = kwargs['code']
        self.__id = kwargs['id'] 
        

    ######################################   
    ###################  Get Method 

    def get_id(self): 
        return self.__id 

    def get_code(self):
        return self.__code 


    ###################################### 
    ###################  Print 

    def __str__(self): 
        return format(self.__id, "<10s")
#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Staff Class                ## 
##        Last updated: 12/26/2022         ##
##                                         ##
#############################################


# Status: 0 - Idle, 1 - Treating 
# Spec: key 

import PersonV2

class Staff(PersonV2.Person):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        self.__spec = kwargs['spec']
        self.__status = kwargs['status']

    ######################################   
    ###################  Get Method 

    def get_spec(self): 
        return self.__spec
    
    ###################################### 
    ###################  Set Method 

    ###################################### 
    ###################  Print 

    def __str__(self): 
        return super().__str__() + format(self.__spec, "<15s") + format(self.__status, "<10d")
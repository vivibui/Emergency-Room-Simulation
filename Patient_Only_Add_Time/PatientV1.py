#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Patient Class              ## 
##                                         ##
#############################################


# Acute level: 1-5 
# Pain level: 1-10 
# Age: 1-105
# Status: 0 - Waiting, 1 - Treating, 2 - Treated 
# Priority Score is calculated in ERSim 

import PersonV1 

class Patient(PersonV1.Person):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        self.__age = kwargs['age']
        self.__acute_level = kwargs['acute_level']
        self.__pain_level = kwargs['pain_level']
        self.__time_coming = kwargs['time_coming']
        self.__status = 0
        self.__time_in_ER = 0
        self.__priority_score = 0
        self.__time_admitted = 0 
        self.__time_released = 0

    ################################################   
    ###################  Get Method ################

    def get_age(self):
        return self.__age 

    def get_acute_level(self):
        return self.__acute_level

    def get_pain_level(self): 
        return self.__pain_level 

    def get_status(self):
        return self.__status 

    def get_time_in_ER(self):
        return self.__time_in_ER

    def get_priority_score(self):
        return self.__priority_score

    def get_time_coming(self):
        return self.__time_coming

    def get_time_admitted(self):
        return self.__time_admitted

    def get_time_released(self):
        return self.__time_released

    
    ################################################   
    ###################  Set Method ################

    def set_priority_score(self, new_score): 
        self.__priority_score = new_score
    
    def set_status(self, new_status): 
        self.__status = new_status 

    def set_time_in_ER(self, new_time): 
        self.__time_in_ER = new_time 

    def deduct_time_in_ER(self): 
        self.__time_in_ER -= 1

    def set_time_admitted(self, new_time): 
        self.__time_admitted = new_time
    
    def set_time_released(self, new_time): 
        self.__time_released = new_time

    ################################################   
    #####################  Print ###################

    def __str__(self): 
        return format(self.__time_coming, "<15d") + super().__str__() \
                + format(self.__age, "<10d") + format(self.__acute_level, "<20d") \
                + format(self.__pain_level, "<20d") + format(self.__status, "<10d") + \
                    format(self.__time_admitted, "<20d") + format(self.__time_released, "<20d")

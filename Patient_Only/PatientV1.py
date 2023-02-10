
# Acute level: 1-5 
# Pain level: 1-10 
# Age: 1-105
# Status: 0 - Waiting, 1 - Treating, 2 - Treated, 3 - LWBS
# Priority Score is calculated in ERSim 

import PersonV1 
from datetime import *


class Patient(PersonV1.Person):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        self.__age = kwargs['age']
        self.__acute_level = kwargs['acute_level']
        self.__pain_level = kwargs['pain_level']
        self.__day_coming = kwargs['day_coming']
        self.__time_coming = None
        self.__status = 0
        self.__length_stay_in_ER = 0 # in minutes 
        self.__priority_score = 0
        self.__day_admitted = 0 # in day
        self.__time_admitted = None
        self.__day_released = 0 # in day 
        self.__time_released = None
        self.__total_wait_time = 0 
        # Note: total_wait_time attribute stores the total minutes a patient have waited before getting treatment
        # Cal_wait_time method returns the wait time at any point of time argument 
        self.__satisfaction_score = 0 

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

    def get_length_stay_in_ER(self):
        return self.__length_stay_in_ER

    def get_priority_score(self):
        return self.__priority_score

    def get_day_coming(self): 
        return self.__day_coming

    def get_time_coming_str(self):
        if self.__time_coming != None: 
            return self.__time_coming.strftime(" %H:%M")
        else: 
            return "TBD"

    def get_time_admitted_str(self):
        if self.get_status() != 3: 
            if self.__time_admitted != None: 
                return self.__time_admitted.strftime(" %H:%M")
            else: 
                return "TBD"
        else: 
            return "LWBS"

    def get_time_released_str(self):
        if self.get_status() != 3: 
            if self.__time_admitted != None: 
                return self.__time_admitted.strftime(" %H:%M")
            else: 
                return "TBD"
        else: 
            return "LWBS"

    def get_time_coming(self): 
        return self.__time_coming

    def get_time_admitted(self):
        return self.__time_admitted

    def get_time_released(self):
        return self.__time_released
    
    def get_total_wait_time(self): 
        return self.__total_wait_time

    def get_satisfaction_score(self): 
        return self.__satisfaction_score

    ################################################   
    ################### Set Method #################

    def set_priority_score(self, new_score): 
        self.__priority_score = new_score
    
    def set_status(self, new_status): 
        self.__status = new_status 

    def set_length_stay_in_ER(self, new_time): 
        self.__length_stay_in_ER = new_time 

    def deduct_time_in_ER(self): 
        self.__length_stay_in_ER -= 1

    def set_time_coming(self, new_time): 
        self.__time_coming = new_time 

    def set_time_admitted(self, new_time): 
        self.__time_admitted = new_time

    def set_day_admitted(self, day): 
        self.__day_admitted = day 

    def set_day_released(self, day): 
        self.__day_released = day 
    
    def set_time_released(self, new_time): 
        self.__time_released = new_time
    
    def set_total_wait_time(self, new_time): 
        self.__total_wait_time = new_time 

    def set_satisfaction_score(self, new_score): 
        self.__satisfaction_score = new_score 

    ################################################   
    ###################  Other Method ##############

    def calc_wait_time(self, current_day, current_time):
        current_delta = timedelta(hours = current_time.hour, minutes = current_time.minute)
        coming_delta = timedelta(hours = self.__time_coming.hour, minutes = self.__time_coming.minute)
        midnight = time(hour = 0, minute = 0)
        midnight_delta = timedelta(hours = midnight.hour, minutes = midnight.minute) 
        if self.__day_coming == current_day: 
            difference =  current_delta - coming_delta 
            return difference.total_seconds()/60 
        else: 
            difference =  (current_delta - midnight_delta).total_seconds()/60 + (24*60 - int(coming_delta.total_seconds()/60))
            return difference 
        

    ################################################   
    #####################  Print ###################

    def __str__(self): 
        return super().__str__()  + format(self.__day_coming, "<10d") + format(self.get_time_coming_str(), "<20s")\
            + format(self.__age, "<10d") + format(self.__acute_level, "<10d") \
                + format(self.__pain_level, "<10d") + format(self.__status, "<10d") \
                    + format(self.__day_admitted, "<10d") + format(self.get_time_admitted_str(), "<20s") \
                        + format(self.__day_released, "<10d") + format(self.get_time_released_str(), "<20s") \
                            + format(self.__length_stay_in_ER, "<20d") + format(self.__total_wait_time, "<20d") \
                                + format(self.__satisfaction_score, "<15.2f") 
     

#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Emergency Room Class       ## 
##        Last updated: 12/26/2022         ##
##                                         ##
#############################################



class EmergencyRoom: 
    def __init__(self, **kwargs): 
        self.__patients = []
        self.__total_beds = kwargs['total_beds']
        self.__open_beds = kwargs['open_beds']

    def get_patients(self): 
        return self.__patients 

    def get_patient(self, id): 
        for patient in self.__patients: 
            if id == patient.get_id(): 
                return patient 
    
    def get_total_beds(self): 
        return self.__total_beds 
    
    def get_open_beds(self): 
        return self.__open_beds

    def bed_taken(self):
        self.__open_beds -= 1 
    
    def bed_release(self): 
        self.__open_beds += 1 

    def count_patients(self):
        count = 0 
        for patient in self.__patients: 
            count+=1 
        return count

    def count_waiting(self):
        count_waiting = 0 
        for patient in self.__patients: 
            if patient.get_status() == 0: 
                count_waiting += 1 
        return count_waiting 

    def count_treating(self):
        count_treating = 0 
        for patient in self.__patients: 
            if patient.get_status() == 1: 
                count_treating += 1 
        return count_treating
    
    def count_treated(self):
        count_treated = 0 
        for patient in self.__patients: 
            if patient.get_status() == 2: 
                count_treated +=1 
        return count_treated 
                
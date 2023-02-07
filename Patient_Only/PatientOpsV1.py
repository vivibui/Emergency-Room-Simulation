#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Patient Operation          ## 
##        Last updated: 02/07/2022         ##
##                                         ##
#############################################


import random 
import PatientV1


def PriorityScore(patient): 
    # Priority order: Acute level -> Age 
    # The lower the score, the higher priority the patient is 

    # Acute Level
    score = 0
    score += patient.get_acute_level()
    # Age group Priority 
    if patient.get_age() <= 10 or patient.get_age() >= 65: 
        score += 0.1
    elif patient.get_age() > 10 and patient.get_age() < 21: 
        score += 0.2 
    else: 
        score += 0.3
    return score 



def NewPatient(p_id, t): 
    p_age = random.randint(1,100) # Max age is 100
    p_acute_level = random.randint(1,5)
    p_pain_level = random.randint(1,10)
    p_code = "P"
    p_time_coming = t
    p_new_patient = PatientV1.Patient(code = p_code, id = p_id, age = p_age, acute_level = p_acute_level, pain_level = p_pain_level, time_coming = p_time_coming)
    p_priority_score = PriorityScore(p_new_patient)
    p_new_patient.set_priority_score(p_priority_score)
    return p_new_patient 



def TimeInER(person): 
    # Set time stay in ER based on pain level
    if person.get_acute_level() == 1: 
        mean_time = 5
    elif person.get_acute_level() == 2: 
        mean_time = 4
    elif person.get_acute_level() == 3: 
        mean_time = 3
    elif person.get_acute_level() == 4: 
        mean_time = 2
    else: 
        mean_time = 1 
    # Set ER time 
    person.set_time_in_ER(mean_time)
#############################################
##                                         ##
##        Emegency Room Simulation         ##
##        Author: Vivian Bui               ## 
##        File: Patient Operation          ## 
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



def NewPatient(p_id, day, t): 
    p_age = random.randint(1,100) # Max age is 100
    p_acute_level = random.randint(1,5)
    p_pain_level = random.randint(1,10)
    p_code = "P"
    p_day_coming = day 
    p_new_patient = PatientV1.Patient(code = p_code, id = p_id, age = p_age, acute_level = p_acute_level, pain_level = p_pain_level, day_coming = p_day_coming)
    p_priority_score = PriorityScore(p_new_patient)
    p_new_patient.set_priority_score(p_priority_score)
    p_new_patient.set_time_coming(t)
    return p_new_patient 



def TimeInER(person): 
    # Set time stay in ER (unit: minutes)
    if person.get_acute_level() == 1: 
        mean_time = random.randint(0,1200) # up to 20 hours 
    elif person.get_acute_level() == 2: 
        mean_time = random.randint(0,900) # up to 15 hours 
    elif person.get_acute_level() == 3: 
        mean_time = random.randint(0,600) # up to 10 hours 
    elif person.get_acute_level() == 4: 
        mean_time = random.randint(0,240) # up to 4 hours 
    else: 
        mean_time = random.randint(0,120) # up to 2 hours 
    # Set ER time 
    person.set_length_stay_in_ER(mean_time)
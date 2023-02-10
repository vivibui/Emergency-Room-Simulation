

# Pain Level converts into points deduction 
def DeductionPoints(pain_level): 
    d_point = 0.1 # lowest deduction point 
    for i in range(0,11): 
        if pain_level == i: 
            return round(d_point,2)
        d_point += 0.01 

# Deduction starts since arrival 
def CalSatisfaction(person, day, time): 
    d_point = DeductionPoints(person.get_pain_level())
    total_wait_time = person.get_total_wait_time() 
    pass

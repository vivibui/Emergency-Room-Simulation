

def DeductionPoints(pain_level): 
    d_point = 0.1 # lowest deduction point 
    for i in range(0,11): 
        if pain_level == i: 
            return round(d_point,2)
        d_point += 0.01 

print(DeductionPoints(10))


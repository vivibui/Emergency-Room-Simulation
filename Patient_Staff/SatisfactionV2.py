

import ConfigV2 as cf 

# Satisfaction is calculated and called when total_wait_time is calculated, meaning: 
    # (1) When a patient get assign to a bed 
    # (2) When a patient decide to leave without being seen (*)


# Pain Level converts into points deduction 
def DeductionPoints(pain_level): 
    d_point = 0.1 # lowest deduction point 
    for i in range(0,11): 
        if pain_level == i: 
            return round(d_point,2)
        d_point += 0.01 

'''
# METHOD 1: Deduction starts since arrival
    # Every 5 minutes, satisfaction score will be deducted by d_point
    # In this scenario, maximum minutes waiting before a patient decide whether to LWBS is 125 minutes
def CalSatisfaction(person): 
    d_point = DeductionPoints(person.get_pain_level())
    total_wait_time = person.get_total_wait_time() 
    score = 5 - (total_wait_time/5)*d_point
    person.set_satisfaction_score(score)
    return score 
'''


# METHOD 2: Deduction starts after BENCHMARK_D 
    # After BENCHMARK_D, every extra 5 minutes will deduct satisfaction score by d_point
    # In this scenario, maximum minutes waiting before a patient decide whether to LWBS is (125+BENCHMARK_D) minutes
def CalSatisfaction(person): 
    d_point = DeductionPoints(person.get_pain_level())
    total_wait_time = person.get_total_wait_time()
    difference = total_wait_time - cf.BENCHMARK_D
    if difference <= 0: 
        score = 5
    else: 
        score = 5 - (difference/5)*d_point 
    person.set_satisfaction_score(score)
    return score 


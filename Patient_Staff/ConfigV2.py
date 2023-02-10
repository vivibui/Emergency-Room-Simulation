

# Description: store all global variables to be used across modules 

# Max days to run simulation 
MAX_DAYS = 3
# Max patients coming in an hour  
    # the larger the number, the easier to check for LWBS, wait time, and satisfaction calculation 
MAX_PATIENTS = 5 
# Initial Condition: ER Capacity 
AVAIL_BEDS = 15
# Benchmark of wait time 
BENCHMARK_W = 100 # minutes 
# Benchmark of wait time before the satisfaction score started to get deducted (METHOD 2)
BENCHMARK_D = 30
# Benchmark of wait time when patient decide whether to leave the ER 
BENCHMARK_L = 125 + BENCHMARK_D # remove BENCHMARK_D if using method 1 for SF Calculation 
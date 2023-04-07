
# Description: store all global variables to be used across modules 

# Max days to run simulation 
MAX_DAYS = 15
# Max patients coming in an hour  
    # the larger the number, the easier to check for LWBS, wait time, and satisfaction calculation 
MAX_PATIENTS = 5 
# Initial Condition: ER Capacity 
AVAIL_BEDS = 8
# Benchmark of wait time (used in Combination Method - Queue module)
BENCHMARK_W = 240 # minutes 
# Benchmark of wait time before the satisfaction score started to get deducted (METHOD 2)
BENCHMARK_D = 30
# Benchmark of wait time when patient decide to leave the ER 
MAX_WAIT = 720
BENCHMARK_L = MAX_WAIT + BENCHMARK_D # remove BENCHMARK_D if using method 1 for SF Calculation 

##########################################################
#################### FOR SELECT QUEUE ####################
##########################################################


###### For Z2-PQ and Z3-Q

# Specify number of probes  
PROBES = 4

# OPTIONAL: Specify order of each probe (as list). First probe is 1.
# PROBES_ORDER = [2,1,4,3]          # <------- Uncomment this if not using default calculation
# Default calculation
all_probes = []
PROBES_ORDER = []
flag_probe = 0
for i in range(PROBES):
    all_probes.append((i+1))
while all_probes: 
    if flag_probe == 0: 
        PROBES_ORDER.append(all_probes.pop(0))
        flag_probe = 1
    if flag_probe == 1: 
        PROBES_ORDER.append(all_probes.pop(-1))
        flag_probe = 0 

    




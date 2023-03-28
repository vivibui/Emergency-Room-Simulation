
import MainV1
import sys
import random 

sim = 1

# Run multiple sim 
for i in range(sim):
    # RANDOM SEED
    n_seed = random.randrange(sys.maxsize)
    random.seed(n_seed)
    MainV1.main(n_seed) 

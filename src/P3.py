from classes.world import world
import numpy as np
from tqdm import tqdm
from classes.ValueIteration import ValueIteration

vi = ValueIteration()

# print("initial:")
#vi.display()

i = 0
while not vi.iterate():
    i += 1

policy = vi.getPolicy()

for i in range(len(policy)):
    for j in range(len(policy[i])):
        print("[",policy[i][j],"]",end='')
        
    print("")
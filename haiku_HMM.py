from HMM_helper import *
from HMM import *
import random
import numpy as np

# Parse the text file
f = open('data/shakespeare.txt')
obs, obs_map = parse_observations(f.read())
f.close()
X = obs

# Parse the A and O matrices
A = np.loadtxt('HMM_A.txt')
O = np.loadtxt('HMM_O.txt')

# Create the model
HMM = HiddenMarkovModel(A, O)

# Generate the sonnet
poem = [] 
poem.append(sample_N_syllables(HMM, obs_map, 5))
poem.append(sample_N_syllables(HMM, obs_map, 7))
poem.append(sample_N_syllables(HMM, obs_map, 5))


for line in poem:
    print(line)
"""

f = open("shakespeare_sonnet.txt", "w")
for i in range(3):
    f.write(couplets[2 * i][0] + "\n")
    f.write(couplets[2 * i + 1][0] + "\n")
    f.write(couplets[2 * i][1] + "\n")
    f.write(couplets[2 * i + 1][1] + "\n")
f.write(couplets[6][0] + "\n")
f.write(couplets[6][1] + "\n")
f.close()
"""
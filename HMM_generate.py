from HMM_helper import *
from HMM import *
from makeRhymeDic import getRhymeDicShakes
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
couplets = [] 
for i in range(7):
    couplets.append(sample_shakes_couplet(HMM, obs_map, 10))
print()


f = open("shakespeare_sonnet.txt", "w")
for i in range(3):
    f.write(couplets[2 * i][0] + "\n")
    f.write(couplets[2 * i + 1][0] + "\n")
    f.write(couplets[2 * i][1] + "\n")
    f.write(couplets[2 * i + 1][1] + "\n")
f.write(couplets[6][0] + "\n")
f.write(couplets[6][1] + "\n")
f.close()

visualize_sparsities(HMM)
states_to_wordclouds(HMM, obs_map)
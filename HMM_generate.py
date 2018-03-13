from HMM_helper import *
from HMM import *
from makeRhymeDic import getRhymeDic
import random
import numpy as np

# Parse the text file
f = open('data/shakespeare.txt')
obs, obs_map = parse_observations(f.read())
X = obs

# Parse the A and O matrices
A = np.loadtxt('HMM_A.txt')
O = np.loadtxt('HMM_O.txt')

# Create the model
HMM = HiddenMarkovModel(A, O)

# Generate the sonnet
couplets = [] 
for i in range(7):
    couplets.append(sample_couplet(HMM, obs_map, 10))
print()

for i in range(3):
    print(couplets[2 * i][0])
    print(couplets[2 * i + 1][0])
    print(couplets[2 * i][1])
    print(couplets[2 * i + 1][1])
print(couplets[6][0])
print(couplets[6][1])

visualize_sparsities(HMM)
states_to_wordclouds(HMM, obs_map)
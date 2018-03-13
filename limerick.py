from HMM_helper import *
from HMM import *
import random
import numpy as np

# Parse the text file
f = open('./data/shakespeare.txt')
obs, obs_map = parse_observations(f.read())
f.close()
X = obs

# Parse the A and O matrices
A = np.loadtxt('HMM_A.txt')
O = np.loadtxt('HMM_O.txt')

# Create the model
HMM = HiddenMarkovModel(A, O)

# Generate the sonnet
# print(poem)
poem = sample_limerick(HMM, obs_map, 10)

f = open("./generated_poems/limerick.txt", "w")

for line in poem:
    f.write(line + "\n")

f.close()
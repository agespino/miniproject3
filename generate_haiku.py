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

# When we use HMM_A.txt and HMM_O.txt we are using 1000 iter
# to generate the haiku 
# When we use haiku_HMM_A.txt and haiku_HMM_O.txt we are 
# using 100 iter to generate the haiku

# Create the model
HMM = HiddenMarkovModel(A, O)

# Generate the sonnet

poem = [] 
poem.append(sample_N_syllables(HMM, obs_map, 5))
poem.append(sample_N_syllables(HMM, obs_map, 7))
poem.append(sample_N_syllables(HMM, obs_map, 5))

f = open("generated_poems/haiku.txt", "w")

for line in poem:
    f.write(line + "\n")

f.close()

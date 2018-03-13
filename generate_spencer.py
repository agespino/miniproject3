from HMM_helper import *
from HMM import *
from makeRhymeDic import getRhymeDicShakes
import random
import numpy as np

# Parse the text file
def parse_observations(text):
    # Convert text to dataset.
    lines = [line.split() for line in text.split('\n') if line.split()]

    obs_counter = 0
    obs = []
    obs_map = {}

    for line in lines:
        obs_elem = []
        if len(line) == 2:
            continue
        for word in line:
            word = ''.join([char for char in word if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'-"]).lower()
            if word not in obs_map:
                # Add unique words to the observations map.
                obs_map[word] = obs_counter
                obs_counter += 1
            
            # Add the encoded word.
            obs_elem.append(obs_map[word])
        
        # Add the encoded sequence.
        obs.append(obs_elem)

    return obs, obs_map

# Parse the text file
f = open('./data/spenser.txt')
obs, obs_map = parse_observations(f.read())
f.close()
X = obs

# Parse the A and O matrices
A = np.loadtxt('spencer_HMM_A.txt')
O = np.loadtxt('spencer_HMM_O.txt')

# Create the model
HMM = HiddenMarkovModel(A, O)

# Generate the sonnet
couplets = [] 
for i in range(7):
    couplets.append(sample_spenser_couplet(HMM, obs_map, 10))
print()


f = open("spencer_sonnet.txt", "w")
for i in range(3):
    f.write(couplets[2 * i][0] + "\n")
    f.write("    " + couplets[2 * i + 1][0] + "\n")
    f.write("    " + couplets[2 * i][1] + "\n")
    f.write("    " + couplets[2 * i + 1][1] + "\n")
f.write(couplets[6][0] + "\n")
f.write("    " + couplets[6][1] + "\n")
f.close()

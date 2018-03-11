from HMM_helper import *
from HMM import *
from makeRhymeDic import getRhymeDicSpencer
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

f = open('data/spenser.txt')
obs, obs_map = parse_observations(f.read())
X = obs

# Initialize the parameters
N_states = 10
N_iters = 1000


L = N_states
D = len(obs_map) + 1

# Randomly initialize and normalize matrix A.
A = [[random.random() for i in range(L)] for j in range(L)]

for i in range(len(A)):
    norm = sum(A[i])
    for j in range(len(A[i])):
        A[i][j] /= norm

# Randomly initialize and normalize matrix O.
O = [[random.random() for i in range(D)] for j in range(L)]

for i in range(len(O)):
    norm = sum(O[i])
    for j in range(len(O[i])):
        O[i][j] /= norm

# Train an HMM with unlabeled data.
HMM = HiddenMarkovModel(A, O)
print('Running ...')
HMM.unsupervised_learning(X, N_iters)

# Save the model
np.savetxt('spencer_HMM_A.txt', HMM.A)
np.savetxt('spencer_HMM_O.txt', HMM.O)
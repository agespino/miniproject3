from HMM_helper import *
from HMM import *
from makeRhymeDic import getRhymeDic
import random
import numpy as np

# Parse the text file
f = open('data/shakespeare.txt')
X, obs_map = parse_observations(f.read())
print('Training size: ', len(X))

# Initialize the parameters
N_states = 8
N_iters = 100
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
np.savetxt('HMM_A.txt', HMM.A)
np.savetxt('HMM_O.txt', HMM.O)
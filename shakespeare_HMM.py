from HMM_helper import *
from HMM import *
import random
import numpy as np

def syllable_dict(filename):
    """ This function will parse the syllable dictionary file and return a
    dictionary where each word is mapped to its syllable count. """
    syllables = {}
    with open(filename) as f:
        for line_of_text in f:
            line = line_of_text.split()
            if len(line) > 2:
                syllables[line[0]] = int(line[2])
            else:
                syllables[line[0]] = int(line[1])
    return syllables

# Compute L and D.
f = open('data/shakespeare.txt')
obs, obs_map = parse_observations(f.read())
X = obs

N_states = 10
N_iters = 100

L = N_states
D = len(obs_map) 

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
HMM.unsupervised_learning(X, N_iters)

for i in range(14):
    print(sample_sentence(HMM, obs_map, 10))

from HMM_helper import *
from HMM import *
from makeRhymeDic import getRhymeDic
import random
import numpy as np

"""
def syllable_dict(filename):"""
""" This function will parse the syllable dictionary file and return a
    dictionary where each word is mapped to its syllable count. """
"""
    syllables = {}
    with open(filename) as f:
        for line_of_text in f:
            line = line_of_text.split()
            if len(line) > 2:
                syllables[line[0]] = int(line[2])
            else:
                syllables[line[0]] = int(line[1])
    return syllables
"""

# Compute L and D.
f = open('data/shakespeare.txt')
obs, obs_map = parse_observations(f.read())
X = obs

N_states = 10
N_iters = 100

L = N_states
D = len(obs_map) + 1
# print(obs_map)

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

# print(np.shape(O)) print D
# print(L) print L
# print(D)

# Train an HMM with unlabeled data.
HMM = HiddenMarkovModel(A, O)
HMM.unsupervised_learning(X, N_iters)

couplets = [] 
for i in range(7):
    couplets.append(sample_couplet(HMM, obs_map, 10))
print()
"""
for i in range(7):
    print(couplets[i][0])
    print(couplets[i][1])
print("\n")
"""

for i in range(3):
    print(couplets[2*i][0])
    print(couplets[2*i+1][0])
    print(couplets[2*i][1])
    print(couplets[2*i+1][1])
print(couplets[6][0])
print(couplets[6][1])

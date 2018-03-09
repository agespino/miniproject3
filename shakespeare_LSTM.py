# Reference: https://machinelearningmastery.com/text-generation-lstm-recurrent
# -neural-networks-python-keras/

import numpy as np 
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# Load text 
filename = 'data/shakespeare.txt'
raw_text = open(filename).read()
# Get rid of integers
raw_text = ''.join([i for i in raw_text if not i.isdigit()])
# Convert to lowercase
raw_text = raw_text.lower()

# Create a mapping of unique characters to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

# Summarize dataset
n_chars = len(raw_text)
n_vocab = len(chars)
print('Total Characters: ', n_chars)
print('Total Vocab: ', n_vocab)

# Prepare the dataset of input to output pairs encoded as integers
seq_length = 40
dataX = []
dataY = []
# How many characters to skip. Increase to speed up training
step_size = 1
for i in range(0, n_chars - seq_length, step_size):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in]) 
    dataY.append(char_to_int[seq_out])
print('Total Patterns: ', len(dataX))

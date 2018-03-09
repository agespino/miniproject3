# Reference: https://machinelearningmastery.com/text-generation-lstm-recurrent
# -neural-networks-python-keras/

# Create model and fit the data

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
n_patterns = len(dataX)
print('Total Patterns: ', n_patterns)

# Reshape the data to be (samples, time steps, features)
X = np.reshape(dataX, (n_patterns, seq_length, 1))
# Normalize
X = X / float(n_vocab)
# One hot encode output variable
y = np_utils.to_categorical(dataY)


# Define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
# model.add(Lambda(lambda x: x / temp))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Define the save point
filepath = 'weights.hdf5'
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, 
    save_best_only=True, mode='min')
callbacks_list = [checkpoint]

# Fit the data
model.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)
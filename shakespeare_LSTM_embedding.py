# Reference: https://machinelearningmastery.com/use-word-embedding-layers-deep
# -learning-keras/

from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
 
# Load doc into memory
def load_doc(filename):
    # Open the file as read only
    file = open(filename, 'r')
    # Read all text
    text = file.read()
    # Close the file
    file.close()
    return text
 
# Load
in_filename = 'shakespeare_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
 
# Integer encode sequences of words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
# Vocabulary size
vocab_size = len(tokenizer.word_index) + 1
 
# Separate into input and output
sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]
 
# Define model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dropout(0.2))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# Load the model
model = load_model('model.h5')
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit model
model.fit(X, y, batch_size=128, epochs=50)
 
# Save the model to file
model.save('model.h5')
# Save the tokenizer
dump(tokenizer, open('tokenizer.pkl', 'wb'))
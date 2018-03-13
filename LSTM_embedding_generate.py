# Reference: https://machinelearningmastery.com/use-word-embedding-layers-deep
# -learning-keras/

from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np
 
# Load doc into memory
def load_doc(filename):
    # Open the file as read only
    file = open(filename, 'r')
    # Read all text
    text = file.read()
    # Close the file
    file.close()
    return text
 
# Generate a sequence from a language model
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    result = list()
    in_text = seed_text
    # Generate a fixed number of words
    for _ in range(n_words):
        # Encode the text as integer
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        # Truncate sequences to a fixed length
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        # Predict probabilities for each word
        preds = model.predict(encoded, verbose=0)
        yhat = np.random.choice(range(len(np.ravel(preds))),p=np.ravel(preds))
        # Map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # Append to input
        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)
 
# Load cleaned text sequences
in_filename = 'shakespeare_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1
 
# Load the model
model = load_model('model.h5')
 
# Load the tokenizer
tokenizer = load(open('tokenizer.pkl', 'rb'))
 
# Select a seed text
seed_text = "shall i compare thee to a summer's day?\n"
print(seed_text + '\n')
 
# Generate new text
for i in range(14):
    print(generate_seq(model, tokenizer, seq_length, seed_text, 10))
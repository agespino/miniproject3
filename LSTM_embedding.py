# Reference: https://machinelearningmastery.com/use-word-embedding-layers-deep
# -learning-keras/

import string
 
# Load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# Turn a doc into clean tokens
def clean_doc(doc):
	# Replace '--' with a space ' '
	doc = doc.replace('--', ' ')
	# Split into tokens by white space
	tokens = doc.split()
	# Remove punctuation from each token
	table = str.maketrans('', '', string.punctuation)
	tokens = [w.translate(table) for w in tokens]
	# Remove remaining tokens that are not alphabetic
	tokens = [word for word in tokens if word.isalpha()]
	# Make lower case
	tokens = [word.lower() for word in tokens]
	return tokens
 
# Save tokens to file, one dialog per line
def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()
 
# Load document
in_filename = 'data/shakespeare.txt'
doc = load_doc(in_filename)
print(doc[:200])
 
# Clean document
tokens = clean_doc(doc)
print(tokens[:200])
print('Total Tokens: %d' % len(tokens))
print('Unique Tokens: %d' % len(set(tokens)))
 
# Organize into sequences of tokens
length = 50 + 1
sequences = list()
for i in range(length, len(tokens)):
	# select sequence of tokens
	seq = tokens[i-length:i]
	# convert into a line
	line = ' '.join(seq)
	# store
	sequences.append(line)
print('Total Sequences: %d' % len(sequences))
 
# Save sequences to file
out_filename = 'shakespeare_sequences.txt'
save_doc(sequences, out_filename)
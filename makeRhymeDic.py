
def getRhymeDicShakes():

	f = open("./data/shakespeare.txt", "r")

	rhym_dic = {}
	poem_line = 0
	poem_last_words = []
	sonnet_num = 0


	for line in f: 
		words = line.split()
		if len(words) == 1:
			# end of sonnet , process sonnet
			if sonnet_num > 0 and sonnet_num != 126 and sonnet_num != 99:
				if poem_last_words[0] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[0]].append(poem_last_words[2])
				else: 
					rhym_dic[poem_last_words[0]] = [poem_last_words[2]]

				if poem_last_words[2] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[2]].append(poem_last_words[0])
				else: 
					rhym_dic[poem_last_words[2]] = [poem_last_words[0]]


				if poem_last_words[1] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[1]].append(poem_last_words[3])
				else: 
					rhym_dic[poem_last_words[1]] = [poem_last_words[3]]

				if poem_last_words[3] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[3]].append(poem_last_words[1])
				else: 
					rhym_dic[poem_last_words[3]] = [poem_last_words[1]]


				if poem_last_words[4] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[4]].append(poem_last_words[6])
				else: 
					rhym_dic[poem_last_words[4]] = [poem_last_words[6]]

				if poem_last_words[6] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[6]].append(poem_last_words[4])
				else: 
					rhym_dic[poem_last_words[6]] = [poem_last_words[4]]


				if poem_last_words[5] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[5]].append(poem_last_words[7])
				else: 
					rhym_dic[poem_last_words[5]] = [poem_last_words[7]]

				if poem_last_words[7] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[7]].append(poem_last_words[5])
				else: 
					rhym_dic[poem_last_words[7]] = [poem_last_words[5]]


				if poem_last_words[8] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[8]].append(poem_last_words[10])
				else: 
					rhym_dic[poem_last_words[8]] = [poem_last_words[10]]

				if poem_last_words[10] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[10]].append(poem_last_words[8])
				else: 
					rhym_dic[poem_last_words[10]] = [poem_last_words[8]]


				if poem_last_words[9] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[9]].append(poem_last_words[11])
				else: 
					rhym_dic[poem_last_words[9]] = [poem_last_words[11]]

				if poem_last_words[11] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[11]].append(poem_last_words[9])
				else: 
					rhym_dic[poem_last_words[11]] = [poem_last_words[9]]


				if poem_last_words[12] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[12]].append(poem_last_words[13])
				else: 
					rhym_dic[poem_last_words[12]] = [poem_last_words[13]]

				if poem_last_words[13] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[13]].append(poem_last_words[12])
				else: 
					rhym_dic[poem_last_words[13]] = [poem_last_words[12]]
			"""	
			elif sonnet_num == 126:
				rhym_dic[poem_last_words[0]] = poem_last_words[1]
				rhym_dic[poem_last_words[1]] = poem_last_words[0]

				rhym_dic[poem_last_words[3]] = poem_last_words[2]
				rhym_dic[poem_last_words[2]] = poem_last_words[3]

				rhym_dic[poem_last_words[4]] = poem_last_words[5]
				rhym_dic[poem_last_words[5]] = poem_last_words[4]

				rhym_dic[poem_last_words[6]] = poem_last_words[7]
				rhym_dic[poem_last_words[7]] = poem_last_words[6]

				rhym_dic[poem_last_words[8]] = poem_last_words[9]
				rhym_dic[poem_last_words[9]] = poem_last_words[8]

				rhym_dic[poem_last_words[10]] = poem_last_words[11]
				rhym_dic[poem_last_words[11]] = poem_last_words[10]
				
			elif sonnet_num == 99:
				rhym_dic[poem_last_words[0]] = poem_last_words[2]
				rhym_dic[poem_last_words[2]] = poem_last_words[0]
				rhym_dic[poem_last_words[0]] = poem_last_words[4]				
				rhym_dic[poem_last_words[4]] = poem_last_words[0]
				rhym_dic[poem_last_words[2]] = poem_last_words[4]
				rhym_dic[poem_last_words[4]] = poem_last_words[2]

				rhym_dic[poem_last_words[1]] = poem_last_words[3]
				rhym_dic[poem_last_words[3]] = poem_last_words[1]

				rhym_dic[poem_last_words[5]] = poem_last_words[7]
				rhym_dic[poem_last_words[7]] = poem_last_words[5]

				rhym_dic[poem_last_words[8]] = poem_last_words[6]
				rhym_dic[poem_last_words[6]] = poem_last_words[8]

				rhym_dic[poem_last_words[9]] = poem_last_words[11]
				rhym_dic[poem_last_words[11]] = poem_last_words[9]

				rhym_dic[poem_last_words[12]] = poem_last_words[10]
				rhym_dic[poem_last_words[10]] = poem_last_words[12]

				rhym_dic[poem_last_words[14]] = poem_last_words[13]
				rhym_dic[poem_last_words[13]] = poem_last_words[14] """

			# move on to next poem 
			poem_line = 0
			poem_last_words = []
			sonnet_num = int(words[0])
		elif len(words) != 0:
			last_word = words[len(words) - 1]
			last_word = ''.join([char for char in last_word if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'-"])
			poem_last_words.append(last_word) 


	f.close()

	return rhym_dic


def getRhymeDicSpencer():

	f = open("./data/spenser.txt", "r")

	rhym_dic = {}
	poem_line = 0
	poem_last_words = []
	sonnet_num = 0


	for line in f: 
		words = line.split()
		if len(words) == 1:
			# print(poem_last_words)
		# end of sonnet , process sonnet
			if sonnet_num > 0 and words[0] != "LXXXV":
				# print(line)
				if poem_last_words[0] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[0]].append(poem_last_words[2])
				else: 
					rhym_dic[poem_last_words[0]] = [poem_last_words[2]]

				if poem_last_words[2] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[2]].append(poem_last_words[0])
				else: 
					rhym_dic[poem_last_words[2]] = [poem_last_words[0]]


				if poem_last_words[1] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[1]].append(poem_last_words[3])
				else: 
					rhym_dic[poem_last_words[1]] = [poem_last_words[3]]

				if poem_last_words[3] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[3]].append(poem_last_words[1])
				else: 
					rhym_dic[poem_last_words[3]] = [poem_last_words[1]]


				if poem_last_words[4] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[4]].append(poem_last_words[6])
				else: 
					rhym_dic[poem_last_words[4]] = [poem_last_words[6]]

				if poem_last_words[6] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[6]].append(poem_last_words[4])
				else: 
					rhym_dic[poem_last_words[6]] = [poem_last_words[4]]


				if poem_last_words[5] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[5]].append(poem_last_words[7])
				else: 
					rhym_dic[poem_last_words[5]] = [poem_last_words[7]]

				if poem_last_words[7] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[7]].append(poem_last_words[5])
				else: 
					rhym_dic[poem_last_words[7]] = [poem_last_words[5]]


				if poem_last_words[8] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[8]].append(poem_last_words[10])
				else: 
					rhym_dic[poem_last_words[8]] = [poem_last_words[10]]

				if poem_last_words[10] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[10]].append(poem_last_words[8])
				else: 
					rhym_dic[poem_last_words[10]] = [poem_last_words[8]]


				if poem_last_words[9] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[9]].append(poem_last_words[11])
				else: 
					rhym_dic[poem_last_words[9]] = [poem_last_words[11]]

				if poem_last_words[11] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[11]].append(poem_last_words[9])
				else: 
					rhym_dic[poem_last_words[11]] = [poem_last_words[9]]


				if poem_last_words[12] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[12]].append(poem_last_words[13])
				else: 
					rhym_dic[poem_last_words[12]] = [poem_last_words[13]]

				if poem_last_words[13] in rhym_dic.keys(): 
					rhym_dic[poem_last_words[13]].append(poem_last_words[12])
				else: 
					rhym_dic[poem_last_words[13]] = [poem_last_words[12]]


			# move on to next poem 
			poem_line = 0
			poem_last_words = []
			sonnet_num += 1
		elif len(words) > 1:
			last_word = words[len(words) - 1]
			last_word = ''.join([char for char in last_word if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'-"])
			poem_last_words.append(last_word) 


	f.close()

	return rhym_dic

		
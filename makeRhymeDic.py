

def getRhymeDic():

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
				rhym_dic[poem_last_words[0]] = poem_last_words[2]
				rhym_dic[poem_last_words[2]] = poem_last_words[0]

				rhym_dic[poem_last_words[1]] = poem_last_words[3]
				rhym_dic[poem_last_words[3]] = poem_last_words[1]

				rhym_dic[poem_last_words[4]] = poem_last_words[6]
				rhym_dic[poem_last_words[6]] = poem_last_words[4]

				rhym_dic[poem_last_words[5]] = poem_last_words[7]
				rhym_dic[poem_last_words[7]] = poem_last_words[5]

				rhym_dic[poem_last_words[8]] = poem_last_words[10]
				rhym_dic[poem_last_words[10]] = poem_last_words[8]

				rhym_dic[poem_last_words[9]] = poem_last_words[11]
				rhym_dic[poem_last_words[11]] = poem_last_words[9]

				rhym_dic[poem_last_words[12]] = poem_last_words[13]
				rhym_dic[poem_last_words[13]] = poem_last_words[12]
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

	
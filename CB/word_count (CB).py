#program: word count

def word_count(sentence):

	txt = sentence.split(' ')
	print len(txt)

user_txt = raw_input("Sentence: ")

word_count(user_txt)
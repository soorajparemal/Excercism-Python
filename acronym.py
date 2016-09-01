w=raw_input("Enter the word : ")
word=w.upper()
acro=list(word.split(" "))
for word in acro:
	print word[0],

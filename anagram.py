w=raw_input("Enter the word : ")
p=raw_input("Enter the possibilities seperated by comma : ")
word=sorted(w)
possibilities=list(p.split(","))
for pos in possibilities:
	if word == sorted(pos):
		print"--> ", pos


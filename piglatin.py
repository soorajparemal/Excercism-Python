x=raw_input("Enter a word : ")
pig='ay'
if len(x)>0 and x.isalpha():
	word=x.lower()
	first=word[0]
	if first == ('a' or 'e' or 'i'or 'o' or 'u'):
		new=word+pig
		print new
	else:
		new=word[1:]+first+pig
		print new
else:
	print "Empty"

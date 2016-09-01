import re
x=raw_input("Enter the phrase : ")
phrase=list(x.split(" "))
dict={}
for sentence in phrase:
	for word in re.split('\s',sentence):
		try:
			dict[word] += 1
		except KeyError:
			dict[word] = 1


print "Word Count --> " , dict
		

	

one=raw_input("Enter the Parent List (seperated by comma) : ")
o=list(one.split(','))
two=raw_input("Enter the Sublist to be checked (seperated by comma) : ")
t=list(two.split(','))
def sublist(one,two):
	y=all(x in o for x in t)
	if y==True:
		print t," Is a sublist of ",o
	elif y==False:
		print t," Not a sublist of",o
	else:
		print "Result unknown"
sublist(one,two)

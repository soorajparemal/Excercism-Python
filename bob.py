question=raw_input("Hi I,m Bob . Wanna ask something ? ")
if question.endswith('?'):
	print "Sure."
elif question.endswith("!"):
	print "WHOA , chill out !"
elif question == "bob":
	print "Fine.Be that way.Nothing to ask!"
else:
	print "Whatever."

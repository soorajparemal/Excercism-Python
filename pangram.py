phrase=raw_input("Enter the phrase : ")
def is_pangram(phrase):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in phrase:
			return False
if is_pangram(phrase)==True:
	print phrase, " Is pangram"
else:
	print phrase, " Is not pangram"

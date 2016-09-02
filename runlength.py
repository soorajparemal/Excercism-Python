text=raw_input("Enter the text to be Encoded  : ")
def encode(text):
	if not text:
		return ""
	else:
		last_char = text[0]
		max_index = len(text)
		i = 1
		while i < max_index and last_char == text[i]:
			i += 1
		return last_char + str(i) + encode(text[i:])

print(encode(text))

text1=raw_input("Enter the text to be Decoded :")

def decode(text1):
	if not text1:
		return ""
	else:
		char = text1[0]
		quantity = text1[1]
		return char * int(quantity) + decode(text1[2:])

print(decode(text1))


x=int(input("Enter the integer : "))
def trans(x):
    	if x == 0: return [0]
    	bit = []
    	while x:
        	bit.append(x % 2)
        	x >>= 1
    	return bit[::-1]
print trans(x)
secret= trans(x) 
handshake=[]
if secret==[1]:
	handshake.append('Wink')
elif secret==[1,0]:
	handshake.append('Double Blink')
elif secret==[1,0,0]:
	handshake.append('Close Your Eyes')
elif secret==[1,0,0,0]:
	habdshake.append('Jump')
else:
	print "Do i know you?"
	

print handshake

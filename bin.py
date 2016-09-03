print ">>>>>Binary --> Integer<<<<"
y=raw_input("Enter a valid Binary number :")
if y!="":
	try:
		print int(y,2)	
	except ValueError:
		print "Asked you to enter a VALID Binary number !. This number is INVALID."
print ">>>>>Integer --> Binary<<<<"
x=int(input("Enter the integer : "))
def trans(x):
    	if x == 0: return [0]
    	bit = []
    	while x:
        	bit.append(x % 2)
        	x >>= 1
    	return bit[::-1]
print trans(x)


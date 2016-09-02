num=raw_input("Enter your phone number(10  or 11 digit number) : ")
numb=list(num)
def IsMobNum(num):
	if len(num)<10:
		print num," Is an Invalid Number ! "
	elif len(num)==10:
		print "The number is valid."
	elif len(num)==11 and numb[0]=='1':
		numb1= ''.join(numb[1:11])
		print 'Valid Number is : ',numb1
	elif len(num)>11:
		print "The number is Invalid ! "
	else :
		print num," Is an invalid number ! "
IsMobNum(num)


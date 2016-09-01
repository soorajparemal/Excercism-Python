year=int(input("Enter the year to be checked : "))
if year%4==0:
	print year, " is Leap year !"
elif year%100==0 :
	if year%400==0:
		print year ," is Leap year !"
	else:
		print year ," is Not leap year."
	
else:
	print year ," is Not leap year ."

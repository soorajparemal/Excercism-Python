x=int(input("Enter the range of numbers (Below 1000 , uses recursion): "))
def sum_of_squares(x):
	if x==0:
		return 0
	else:
		return (x*x)+sum_of_squares(x-1)
	
print "Sum of squares is : ", sum_of_squares(x)

def square_of_sum(x):
	if x<=2:
		return x
	else:
		return square_of_sum(x-1)+x
print "Square of sum is : ", square_of_sum(x)*square_of_sum(x)
print 20*"*"
print "The difference is :----> " , sum_of_squares(x)-square_of_sum(x)
	

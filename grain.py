print ":--: Grain Of Wheat Problem:--:"
num_of_squares=64
def grain(num_of_squares):
	i=2
	for n in range(num_of_squares):
		print 'Number of grains on square ', n+1 ,' is ',i
		i<<=1

grain(num_of_squares)


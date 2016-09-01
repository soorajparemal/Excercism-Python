n=int(input("Enter the Range : "))
def is_prime(n):
	sieve=[True]*(n+1)
	for p in range(2,n+1):
		if(sieve[p]):
			print p
			for i in range(p,n+1,p):
				sieve[i] = False
is_prime(n)

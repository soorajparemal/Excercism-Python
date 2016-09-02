s=raw_input("Enter the triangles sides seperated by comma eg(a,b,c) : ")
sides=map(int,s.split(","))
print sides
def isTriangle(sides):
        small,medium,big=sorted(sides)
        return small+medium>=big and all(s>0 for s in (sides))
print isTriangle(sides) 
a,b,c=sides
if isTriangle(sides)==True:
	if a==b==c:
		print "Equilateral Triangle !"
	elif a!=b!=c:
		print "Scalene Traingle !"
	else:
		print "Isosceles Triangle !"
else:
	print("This Triangle is not possible according to 'Triangle Inequality Theorem' ! ")
	

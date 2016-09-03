def pythagorean():
    for a in xrange(500):
        for b in xrange(a+1,500):
            c=1000-(a+b)
            if a**2+b**2==c**2:
                return a*b*c
print "The product of Pythagorean Triplet for which a+b+c==1000 -s --> ",pythagorean()

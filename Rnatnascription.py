dna=raw_input("Enter the DNA strand sequence(Using A,C,G and T) : ")
DNA=list(dna.upper())
print "The DNA sequence you Entered --> ",dna.upper()
print ": : : The respective RNA transcription in : : : "
for i in DNA:
	if i=='A':
		print 'U',
	elif i=='G':
		print 'C',
	elif i=='C':
		print 'G',
	elif i=='T':
		print 'A',
	else:
		print 'ERROR! --> Invalid Entry',


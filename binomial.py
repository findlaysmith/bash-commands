#!/usr/bin/env python
import sys
def term(n,r):
        from math import factorial
        q = factorial(n)/(factorial(r)*factorial(n-r))
        return(str(q) + "\n")

def general(n):
	term=[]
	from math import factorial
	for r in range(0,n+1):
		q = factorial(n)/(factorial(r)*factorial(n-r))
		term.append(q)
	return(str(term) + "\n")
c = str(sys.argv[1]) #choice of print or file '-p- print '-f' file
n = int(sys.argv[2])
if len(sys.argv) == 3:
        if c == '-f':
                term = general(n)
                x = open('bin.log', 'a')
                x.write(str(term))
		print (str(term) + ' written to bin.log in documents')
        if c == '-p':
                term = general(n)
                print term
elif len(sys.argv) == 4:
	r = int(sys.argv[3])
        if c == '-f':
                term = term(n, r)
                x = open('bin.log', 'a')
                x.write(str(term))
		print (str(term) + ' written to bin.log in documents')
        if c == '-p':
                term = term(n,r)
                print term

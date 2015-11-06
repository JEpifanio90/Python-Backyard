Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def check(x):
	isPrime=True
	for i in range(2,x-1):
		if(x%i==0):
			isPrime=False
	return isPrime

>>> def createPG():
	import random
	p=random.randrange(0,50)
	g=random.randrange(0,50)
	while(not check(p) and not check(g)):
		p=random.randrange(0,50)
		g=random.randrange(0,50)
	return p,g

>>> def gcd(a,b):
        a=max(a,b)
        b=min(a,b)
        if(b==0):
                return a
        else:
                return(b,a%b)

>>>def egcd(a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
                q, r = b//a, b%a
                m, n = x-u*q, y-v*q
                b,a, x,y, u,v = a,r, u,v, m,n
                gcd = b
        return gcd, x, y

>>> def calculateNPhi():
	import random
	prime=createPG()
	n=prime[0]*prime[1]
	phi=(prime[0]-1)*(prime[1]-1)
	while(gcd(e,n)!= 1):
		e=random.randrange(0,50)
	return n,phi,e

>>>def calculateD():
	elements= calculateNPHI()
	d=egcd(elements[0],elements[2])
	return d


>>> def createPG():
	import random
	p=random.randrange(51,999)
	g=random.randrange(51,999)
	while(not check(p) and not check(g)):
		p=random.randrange(3,51)
		g=random.randrange(3,51)
	return p,g

>>> def check(x):
	isPrime=True
	for i in range(2,x-1):
		if(x%i==0):
			isPrime=False
	return isPrime

>>> def gcd(a,b):
	import fractions
	gcd=fractions.gcd(a,b)
	return gcd

        
>>> def egcd(a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
                q, r = b//a, b%a
                m, n = x-u*q, y-v*q
                b,a, x,y, u,v = a,r, u,v, m,n
                gcd = b
        return gcd, x, y

>>>def calculateNPhi():
	import random
	prime=createPG()
	n=prime[0]*prime[1]
	phi=(prime[0]-1)*(prime[1]-1)
	e=random.randrange(1,phi)
	while(gcd(e,n)!= 1):
		e=random.randrange(1,phi)
	return n,phi,e

>>> def calculateD():
	elements= calculateNPhi()
	print("Public key (",elements[2],",",elements[0],")")
	d=egcd(elements[0],elements[2])
	return d[2],elements[0]
#public key (e,n)
#private key (d,n)
>>>def main():
	elem=calculateD()
	print("Private key (",elem[0],",",elem[1],")")
        

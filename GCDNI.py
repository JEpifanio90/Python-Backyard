Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> def gcd(a,b)
SyntaxError: invalid syntax
>>> def gcd(a,b):
	a=max(a,b)
	b=min(a,b)
	while b!=0:
		c=b
		b=a%b
		a=c

		
>>> def gcd(a,b):
	a=max(a,b)
	b=min(a,b)
	while b!=0:
		c=b
		b=a%b
		a=c
	return a

>>> gcd(12,8)
4
>>> 

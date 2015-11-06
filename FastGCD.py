Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import fractions
>>> def fastgcd(a,b)
SyntaxError: invalid syntax
>>> 
>>> def fastgcf(a,b):
	cd=fractions.gcd(a,b)
	print("The gcd of the integers %d and %d is %d" %(a,b,cd))

	
>>> fastgcf(12,8)
The gcd of the integers 12 and 8 is 4
>>> def fastgcd(a,b):
	cd=fractions.gcd(a,b)
	print("The gcd of the integers %d and %d is %d" %(a,b,cd))

	
>>> fastgdc(1234,4321)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fastgdc(1234,4321)
NameError: name 'fastgdc' is not defined
>>> fastgcd(1234,4321)
The gcd of the integers 1234 and 4321 is 1
>>> 

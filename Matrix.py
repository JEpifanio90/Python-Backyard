Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def matrix():
	print("Dame el número de expertos")
	nExp=int(input())
	print("Dame el número de características")
	nCara=int(input())
	Axi=[]
	for i in range(0,nCara):
		print("Dame la característica #: ",i)
		x=int(input())
		Axi.append(x/nCara)
	print("//////// Printing Matrix ////////")
	for i in range(0,nExp-1):
		for j in range(0,nExp):
			print(Axi[i],"/",Axi[j],"--", end=" ")
		print("\n")
		if i==nExp :
			print(Axi[i],"/",Axi[i],"--", end=" ")
		else :
			print(Axi[i],"/",Axi[i+1],"--", end=" ")
	print("....DONE")

	
>>> 

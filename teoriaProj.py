#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'José Epifanio'


class teoriaProj:
	def processFile(self, text):
		chain = ""
		try:
			fp = open(text)
		except:
			print "NO encuentro un archivo con ese nombre."
		flag = False
		for line in fp:
			for character in line.lower():
				if flag == True:
					character = character.upper()
					chain = chain + character
				else:
					chain = chain + character

				if character == " ":
					flag = True
					flag = False
		self.originalChainSize = len(chain)
		self.codeElemental(chain)

	def codeElemental(self, chain):
		dictionary = dict()
		self.listTuple=list()
		self.listOrder = list()
		self.listEncoded=list()
		self.uncodedList = list()
		for element in chain.split():
			dictionary[element] = dictionary.get(element, 0) + 1
			self.listOrder.append(element)
		for element in self.listOrder:
			#print "Element: ", element, " value: ", dictionary[element]
			self.uncodedList.append(((len(element),dictionary[element]),element))

	def encodeText(self):
		print self.uncodedList
		self.codedList = list()
		i=0
		x=0
		for key, value in self.uncodedList:
			if i>=118:
				i=0
				chain = chain+self.listElements[x]
				x=x+1
			chain=self.listElements[i]
			self.codedList.append((key,chain))
			i=i+1

	def printCodedText(self):
		chain=""
		for key,value in self.codedList:
			print "Key: ",key," Value: ",value
			chain = chain + value
		print chain
		print len(chain)

	def getElementList(self):
		self.listElements = list()
		try:
			fp = open("ListOfElements.txt")
		except:
			print "Moviste el .txt de los elementos. Gracias, ahora ya no funciono."
		for line in fp:
			line = line.lower().rstrip()
			self.listElements.append(line)


def main():
	text = raw_input("Give me a text to compress, please :B.")
	teo = teoriaProj()
	teo.getElementList()
	teo.processFile(text)
	teo.encodeText()
	teo.printCodedText()


if __name__ == "__main__":
	main()

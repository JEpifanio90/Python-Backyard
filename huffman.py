#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'Josefoo'
from heapq import heappush, heappop, heapify
from collections import defaultdict

class huffman:

	def encode(symb2freq):
	 heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
	 heapify(heap)
	 while len(heap) > 1:
	     lo = heappop(heap)
	     hi = heappop(heap)
	     for pair in lo[1:]:
	         pair[1] = '0' + pair[1]
	     for pair in hi[1:]:
	         pair[1] = '1' + pair[1]
	     heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
	 return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

	txt = raw_input("Give me a txt file")
	symb2freq = defaultdict(int)
	try:
		txtFile = open(txt)
	except:
		print "No puedo encontrar un archivo con ese nombre."
	for line in txtFile:
		for ch in line:
    		 symb2freq[ch] += 1
		# in Python 3.1+:
		# symb2freq = collections.Counter(txt)
	huff = encode(symb2freq)
	print "Symbol\tWeight\tHuffman Code"
	chain=""
	for p in huff:
    	 print "%s\t       %s\t    %s" % (p[0], symb2freq[p[0]], p[1])
    	 chain=chain+p[0]
	print "Radio de compresión: ",len(huff)
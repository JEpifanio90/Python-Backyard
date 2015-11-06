#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from PIL import Image
import numpy as np
import cv2

class CheetahDetection:
	def __init__(self,image):
		self.imag=image
		self.width=image.size[0]
		self.heigth=image.size[1]
		self.newImage=Image.new(self.imag.mode,self.imag.size)
		self.newAImag=Image.new(self.imag.mode,self.imag.size)


	def grayScale(self):
		for x in range(self.width):
			for y in range(self.heigth):
				red, blue, green = self.imag.getpixel((x,y))
				gray = int(0.21 * red + 0.72 * green + 0.07 * blue)
				self.newImage.putpixel((x,y), (gray, gray, gray))
		self.newImage.save("Images/cheetahGray2.png", self.imag.format)
        print("GrayScale Done...")

	def fourBitThreshold(self):
		print "Starting threshold"
		ran=255/4
		for x in range(self.width):
			for y in range(self.heigth):
				gray = self.newImage.getpixel((x,y))
				gray = gray[0]
				if gray>0 and gray<ran:
					if(ran/2)>gray:
						gray=0
					else:
						gray=ran
				elif gray>ran and gray<(ran*2):
					if((ran*2)/2)>gray:
						gray=ran
					else:
						gray=ran*2
				elif gray>(ran*2) and gray<(ran*3):
					if((ran*3)/2)>gray:
						gray=ran*2
					else:
						gray=ran*3
				elif gray>(ran*3) and gray<(ran*4):
					if ((ran*4)/2)>gray:
						gray=ran*3
					else:
						gray=ran*4
				else:
					gray=255
				self.newAImag.putpixel((x,y),(gray,gray,gray))
		self.newAImag.save("Images/cheetahFourBitThreshold.png", self.imag.format)
		print "Four Bit Threshold Done..."

	def filterBefore(self):
		print "Applying some bilateral Filter."
		img = cv2.imread('Images/cheetahGray2.png')
		bilateral =  cv2.bilateralFilter(img,9,75,75)
		cv2.imwrite('Images/cheetahBilateralFilterBefore.png',bilateral)
		self.newImage.save("Images/cheetahBilateralFilterBefore.png",self.imag.format)
		print "Bilateral Filter Done."

	def secondTime(self):
		print "Applying some bilateral Filter."
		img = cv2.imread('Images/cheetahGaussian.png')
		bilateral =  cv2.bilateralFilter(img,9,75,75)
		bilateral = cv2.medianBlur(bilateral,7)
		bilateral = cv2.GaussianBlur(bilateral,(5,5),0)
		blur = cv2.GaussianBlur(bilateral,(5,5),0)
		cv2.imwrite('Images/cheetahSecongTime.png',bilateral)
		print "Bilateral Filter Done."

	def bilateralFilter(self):
		print "Applying some bilateral Filter."
		img = cv2.imread('Images/cheetahFourBitThreshold.png')
		bilateral =  cv2.bilateralFilter(img,9,75,75)
		bilateral = cv2.medianBlur(bilateral,3)
		bilateral = cv2.GaussianBlur(bilateral,(5,5),0)
		blur = cv2.GaussianBlur(bilateral,(5,5),0)
		cv2.imwrite('Images/cheetahGaussian.png',bilateral)
		print "Bilateral Filter Done."

	def circlesDetection(self):
		print "Detecting Circles"
		img = cv2.imread("Images/cheetahGaussian.png",0)
		img = cv2.medianBlur(img,5)
		cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
		circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:# draw the outer circle
    	 	 cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    		 # draw the center of the circle
    		 cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
		#cv2.imshow('detected circles.png',cimg)
		cv2.imwrite("Images/detected circles.png",cimg)
		print "Circles detection Done."

def main():
	cheetah = CheetahDetection(Image.open("Images/cheetahFace.png"))
	cheetah.grayScale()
	cheetah.filterBefore()
	cheetah.fourBitThreshold()
	cheetah.bilateralFilter()
	#cheetah.circlesDetection()
	cheetah.secondTime()




if __name__=="__main__":
	main()
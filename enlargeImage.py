#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image

class enlargeImage():

    def __init__(self,image):
        self.imag=image
        self.width=image.size[0]
        self.height=image.size[1]
        self.newImag= Image.new(self.imag.mode,self.imag.size)

    def enlarge(self,size):
        for x in range(self.height):
            for y in range(self.width):
                red,green,blue = self.imag.getpixel((x,y))
                x=x+size
                for s in range(size):
                    self.newImag.putpixel((x,y),red,green,blue)


def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    enlarge=enlargeImage(Image.open(str(usrImag)))
    size =int(raw_input("Give me the size you want to enlarge the image"))
    enlarge.enlarge(size)


if __name__=="__name__":
    main()
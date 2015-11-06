#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Josefoo'
def computepay(h,r):
    if h<=40:
        pay=r*h
    else:
        pay=r*40+(r*1.5*(h-40))
    return pay

try:
    hrs = raw_input("Enter Hours:")
    hrs=float(hrs)
    rate= raw_input("Enter Rate:")
    rate=float(rate)
except:
    print("Write only numbers")
    quit()


p = computepay(hrs,rate)
print "Pay",p
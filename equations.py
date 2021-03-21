# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:48:55 2021

@author: Hadar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


    
def XtimesY(x:float, y:float):
    if x<=0:
        return 0.0
    r=exponent(y*Ln(x))
    result= float('%0.6f' % r)
    return result

def exponent(x:float):
    n=1
    ex=1.0
    wowy=1.0
    powy=1.0
    while (n<100):
        powy=powy*x
        wowy=wowy*n
        ex=ex+ powy/wowy
        n=n+1
    return ex

  
def Ln(x:float):
    if x<=0:
        return 0.0
    yn=x-1.0
    yn1=yn+2*(x-exponent(yn))/(x+exponent(yn))
   
    while (x==x):
        dif= yn1-yn
        if dif<0:
            dif=-dif
        if dif>0.000001:
            yn=yn1
            yn1=yn+2*(x-exponent(yn))/(x+exponent(yn))
            dif=yn1-yn
        else:
            return yn1

  
 
def sqrt(x:float, y:float):
    if y<=0:
        return 0.0
    return XtimesY(y, 1/x)


def calculate(x:float):
    if x<=0:
        return 0.0
    r=float('%0.6f' % exponent(x))*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    return r

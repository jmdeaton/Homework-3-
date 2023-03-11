# Authors   : Jordan Deaton
# Emails    : jdeaton@umass.edu
# Spire IDs : 32854417

import math 

def simplify(frac): 
    gcd = math.gcd(frac[0], frac[1])
    p = (frac[0] / gcd , frac[1] / gcd) 
    return p 

def make_fraction(top, bottom):
     f = math.gcd(top, bottom)
     top = top // f
     bottom = bottom // f 
     return(top, bottom)

def add(frac1, frac2): 
     a = frac1[0]
     b = frac1[1]
     c = frac2[0]
     d = frac2[1]
     l = math.lcm(b,d)
     num1 = a * (l//b)
     num2 = c * (l//d)
     top =  num1 + num2 
     frac3 = make_fraction(top, l)
     return simplify(frac3)

print(add((1, 5), (3, 5)))  # This should return (4, 5)
print(add((1, 6), (3, 4)))  # This should return (11, 12)


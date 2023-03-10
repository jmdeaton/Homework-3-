# Authors   : Jordan Deaton
# Emails    : jdeaton@umass.edu
# Spire IDs : 32854417

import math 

def simplify(frac): 
    gcd = math.gcd(frac[0], frac[1])
    p = (frac[0] / gcd , frac[1] / gcd) 
    return p 

print(simplify((2, 10)))  # This should return (1, 5)
print(simplify((5, 13)))  # This should return (5, 13)
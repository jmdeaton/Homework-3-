# Authors   : Jordan Deaton
# Emails    : jdeaton@umass.edu
# Spire IDs : 32854417

def get_input():
    x = input('Input rock, paper, or scissors')
    return x.lower()

def p1_wins(p1, p2):
    if p1 == 'rock' and p2 == 'scissors': 
        return True 
    elif p1 == 'scissors' and p2 == 'paper': 
        return True 
    elif p1 == 'paper' and p2 == 'rock': 
        return True 
    else: 
       return False 
    
def p2_wins(p1, p2):
    return not(p1_wins(p1, p2))

def tie(p1, p2): 
    if p1 == p2: 
        return True 
    else: 
        return False 
    

print(tie('paper', 'paper'))      # This should return True
print(tie('paper', 'rock'))       # This should return False
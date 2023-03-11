# Authors   : Jordan Deaton
# Emails    : jdeaton@umass.edu
# Spire IDs : 32854417

def is_palindrome(s): 
    if s[::-1] == s:
        return True 
    else: 
        return False 

def is_anagram(s, t): 
    if sorted(s) == sorted(t) or sorted(t) == sorted(s):
        return True 
    else: 
        return False 
    
def same_word(s, t):
    if s == t or t == s: 
        return True 
    else: 
        return False 
 
print(same_word('foo', 'Foo')) # This should return True
print(same_word('foo', 'bar')) # This should return False
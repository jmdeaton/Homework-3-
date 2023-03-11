# Authors   : Jordan Deaton
# Emails    : jdeaton@umass.edu
# Spire IDs : 32854417

def list_min(l): 
    return min(l)

def list_max(l): 
    return max(l)

def list_range(l): 
    return max(l) - min(l) 

def list_mean(l): 
    return sum(l) / len(l) 

def list_median(l): 
    return sorted(l)[len(l) // 2]

print(list_median([1, 2, 3]))           # This should return 2
print(list_median([5, 5, 4, 4, 6]))     # This should return 5
print(list_median(['abc', 'ab', 'bc'])) # This should return 'abc'




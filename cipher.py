# Authors   : Jordan Deaton
# Emails    : jdeaton@umass.edu
# Spire IDs : 32854417

def l337_encrypt(s): 
    s = s.replace('O','0')
    s = s.replace('I','1')
    s = s.replace('E','3')
    s = s.replace('A','4')
    s = s.replace('S','5')
    s = s.replace('T','7')
    s = s.replace('B','8')
    return s 

def l337_decrypt(s):
    s = s.replace('0','O')
    s = s.replace('1','I')
    s = s.replace('3','E')
    s = s.replace('4','A')
    s = s.replace('5','S')
    s = s.replace('7','T')
    s = s.replace('8','B')
    return s 

print(l337_decrypt('347'))    # This should return 'EAT'
print(l337_decrypt('M4N4N'))  # This should return 'MANAN'
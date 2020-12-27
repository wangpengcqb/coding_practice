def checkpalindrome(s):
    if not s or len(s) == 1:
        return True
        
    s = s.lstrip(' ').rstrip(' ')
    lo = 0
    hi = len(s)-1
    
    while lo < hi:
        if s[lo].lower() != s[hi].lower():
            return False

        lo += 1
        while not s[lo].isalpha():
            lo += 1
        
        hi -= 1
        while not s[hi].isalpha():
            hi -= 1
        
    return True
        
    
    
a = "   a Bc  DC b  A   "    
print (checkpalindrome(a))
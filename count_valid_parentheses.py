def countvalidparenthese(s):
    if not s or len(s) == 1:
        return 0
        
    left = right = 0
    count = 0
    for c in s:
        if c == '(':
            left += 1
        elif c == ')':
            right += 1
            if right <= left:
                count += 1 
            else:
                left = right = 0
                
    return count 
    
a = 'an(d(c(d)6)f)b)(fa))'
print (countvalidparenthese(a))
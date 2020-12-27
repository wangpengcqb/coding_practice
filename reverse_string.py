def reversestring(s):
    if not s or len(s) == 1 or len(s.split(' ')) == 1:
        return s
        
    start = end = 0 
    res = []
    while end < len(s):
        while end < len(s) and s[end].isalpha():
            end += 1
        if end > start:
            res.append("".join(reversed(s[start:end])))
            
        start = end
        while end < len(s) and not s[end].isalpha():
            end = end + 1
        if end > start:
            res.append(s[start:end])
        start = end
     
    return ''.join(res)
            
        
    
    
    
s = 'I have a pen, I have an apple.'    
    

print(reversestring(s))
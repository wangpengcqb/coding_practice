a = 'SELECT a FROM table WHERE b="a shi; ge" and yes;Select from my table \" life; sucks "yes" ;'

def splitquery(s):
    if not s:
        return s
        
    last = 0
    cur = 0 
    quote = False
    res = []
    while cur < len(s):
        if s[cur] == '\\':
            cur += 2
        elif s[cur] == '"':
            quote = not quote
            cur += 1
        elif not quote and s[cur] == ';':
            res.append(s[last:cur])
            cur += 1 
            last = cur
        else:
            cur += 1
    
    res.append(s[last:])        
    return res
        
    
print(splitquery(a))
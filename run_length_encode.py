def encodestring(a):
    if not a or len(a) == 1:
        return a
        
    start = 0
    end = 0
    
    res = ''
    while end < len(a):
        while end <  len(a) and a[end] == a[start]:
            end += 1
        count = end - start
        res += a[start] + str(count)
        
        start = end
        
    return res
    
a = '111bcc'


print (encodestring(a))
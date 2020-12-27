import bisect
import heapq
import collections


def crush(s):
    if not s or len(s) < 3:
        return s 

    i = 0
    res = []
    while i < len(s):
        res.append(s[i])
        j = -1
        count = 0
        while j >= -len(res) and res[j] == s[i]:
            j -= 1
            count += 1 
        if count >= 3:
            while count > 0:
                res.pop()
                count -= 1
        i += 1
    return ''.join(res)
            
        
a = 'wsdcabbbaaccddsswfds'
print(crush(a))
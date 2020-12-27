def separate(s, dels):
    if not s or not dels:
        return
    dels.sort(key=lambda x: -len(x))
    res = []
    last = 0 
    i = 0 
    while i < len(s):
        for d in dels:
            if s[i:].startswith(d):
                res.append(s[last:i])
                last = i + len(d)
                i = i + len(d)
                break
                
        i += 1
    res.append(s[last:])
    return res

s="abcdefg"
dels=["bc", "f"]

print (separate(s, dels))

s="abcdefg"
dels=["bc", "f", "b"]

print (separate(s, dels))
def findpattern(s, patterns):
    if not s or not patterns:
        return []
    
    res = []
    
    for p in patterns:
        match = kmp(s, p)
        res.append(match)
        
    return res
    
def kmp(s, p):
    j = 0
    res = []
    arr = buildkmp(p)
    for i in range(len(s)):
        if s[i] == p[j]:
            if j == len(p)-1:
                res.append(i-j)
            else:
                i += 1
                j += 1
        else:
            if j > 0:
                j = arr[j-1]
            else:
                i += 1
    return res
    
def buildkmp(p):
    l = 0
    arr = [0 for i in range(len(p))]
    for i in range(1, len(p)):
        while l > 0 and p[i] != p[l]:
            l = arr[l-1]
        if p[i] == p[l]:
            l += 1
            arr[i] = l
    return arr
    
    

s = 'I love AAA love one point AAA three acres'
list_of_strings = ['love', 'acres', 'four', 'AAA']

print (findpattern(s, list_of_strings))


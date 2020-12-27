from collections import defaultdict
def longestCommonPrefix(strings):
    if not strings:
        return ''
        
    i = 0
    res = ''
    
    havecommon = True
    while havecommon:
        mymap = defaultdict(int)
        havecommon = False
        for s in strings:
            if i >= len(s):
                return res
            
            if mymap[s[:i+1]] > 0:
                havecommon = True
                res = s[:i+1]
            mymap[s[:i+1]] += 1
            
        if not havecommon:
            return res
        i += 1
    return res


a = ["bandage", "banana", "anchor", "anchovy", "bass"]
print (longestCommonPrefix(a))
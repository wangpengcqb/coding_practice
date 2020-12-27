import bisect
import collections

def weightedmeetingroom(arr):
    if not arr:
        return []
    
    mymap = collections.defaultdict(int)    
    for m in arr:
        mymap[m[0]] += m[2]
        mymap[m[1]] -= m[2]
        
    mymap = dict(sorted(mymap.items()))
    
    res = []
    start = None
    precount = None
    count = 0
    for k, v in mymap.items():
        count += v
        if precount and count != precount:
            if start:
                res.append([start, k, precount])
            start = k
        
        precount = count
    return res


a = [[1,3,1], [2,4,2], [2,7,3], [4,5,1], [6,9,2]]
b = weightedmeetingroom(a)
    

print (b)
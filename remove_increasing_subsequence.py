from collections import defaultdict
import bisect
def removeIncreasingSubsequence(arr):
    if not arr or len(arr) == 1:
        return []
        
    index = defaultdict(list)
    
    for i, n in enumerate(arr):
        index[n].append(i)
        
    index = dict(sorted(index.items()))
    
    res_index = []
    
    cur_index = 0
    for _, v in index.items():
        if len(v) <= 1:
            continue
        i = bisect.bisect_right(v, cur_index)
        if i > 1:
            return [-1]
        if i == 1:
            res_index.extend(v[1:])
            cur_index = v[-1]
        else: # i == 0
            res_index.extend(v[:-1])
            cur_index = v[-2]
    
    res = []        
    for i in res_index:
        res.append(arr[i])
        
    return res
    


a = [1,2,3,1,2,3,3,6,4]
a = [1,2,3]
a = [1,2,3,3,2,1]
a = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3]
a = [9,9,8,8,7,7,6,5,4,3,2,1]
a = [1,1,1,4,6,6,4,7,8,9]
a = [3,3,4,1,1,5,6,]
a = [1]
a = [4,5,6,3,2,3,4,5,1,5,6,7,]
a = [7,8,7,8,7,8,7,8,7,8,7,8,7,8,7,8]
a = [7,8,9,0]
a = [-1,-1,5,6,-100,float('inf'), -float('inf'),float('inf')]
a = [-1,-1,5,6,-100,float('inf'), -float('inf'),-float('inf')]
a = [5,6,4,3,32,2,1,4,5,6,5,4,3,32,]

print(removeIncreasingSubsequence(a))
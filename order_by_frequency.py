import heapq
import collections

def outputfrequency(arr):
    if not arr or len(arr) == 1:
        return arr 
        
    mymap = collections.defaultdict(int)
    
    for num in arr:
        mymap[num] += 1
        
    h = []
    
    for k, v in mymap.items():
        heapq.heappush(h, (-v, k))
        
    res = []
    
    while h:
        cnt, num = heapq.heappop(h)
        res.extend([num]*(-cnt))
        
    return res
    

a = [3, 2, 3, 1, -1, 2, 3]
print (outputfrequency(a))
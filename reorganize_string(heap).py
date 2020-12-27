from collections import Counter
import heapq
def ReorganizeString(S):
    if not S or len(S) == 1:
        return S
        
    cnt = Counter(S)
    pq = []
    for x, c in cnt.items():
        if c > (len(S)+1)//2:
            return ''
        heapq.heappush(pq, (-c, x))
        
    res = ''
    while len(pq) >= 2:
        c1, x1 = heapq.heappop(pq)
        c2, x2 = heapq.heappop(pq)
        res += x1
        res += x2
        
        if c1 + 1:
            heapq.heappush(pq, (c1+1, x1))
        if c2 + 1:
            heapq.heappush(pq, (c2+1, x2))
            
    if pq:
        c, x = heapq.heappop(pq)
        res += x
        
    return res
    
    

a = 'abbbc'
print (ReorganizeString(a))

b = 'abbbbbbbbbccccrfs'
print (ReorganizeString(b))
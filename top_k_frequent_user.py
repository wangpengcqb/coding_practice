from collections import Counter
import heapq
def TopKUser(log, k):
    if not log or len(log) < k:
        return []
    
    cnt = Counter()    
    for l in log:
        user = l.split(': ')[0]
        cnt[user] += 1
        
    pq = []
    
    for u, c in cnt.items():
        heapq.heappush(pq, (c, u))
        
        if len(pq) > k:
            heapq.heappop(pq)
            
    res = []
    while pq:
        c, u = heapq.heappop(pq)
        res.insert(0, u)
    return res


log = [
"A: hello", 
"B: hi",
"C: nice",
"D: I love it",
"A: What's wrong",
"B: Nothing",
"C: Yep",
"B: Oh yeah",
"D: WTF",
"E: Oh",
"B: N",
"A: time",
"C: over",
"A: What",
"B: my lady",
"F: Life sucks",
]
print (TopKUser(log, 3))
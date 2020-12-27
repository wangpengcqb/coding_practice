from collections import defaultdict
def find_pattern(A, B):
    if not B or not A or len(A) < len(B):
        return []
        
    cnt = len(B)
    record = defaultdict(int)
    
    for c in B:
        record[c] -= 1
    
    start = 0
    end = 0
    res = []

    while end < len(A):
        c = A[end]
        if record[c] < 0:
            cnt -= 1
        record[c] += 1
        end += 1
        
        if cnt == 0:
            res.append(A[start:end])
        
        if end - start == len(B):
            c = A[start]
            if record[c] == 0:
                cnt += 1
            record[c] -= 1
            start += 1
            
    return res
            

A = "abctieowkcbale"
B = "abc"
print(find_pattern(A, B))

A = "abatieowkabale"
B = "aab"
print(find_pattern(A, B))
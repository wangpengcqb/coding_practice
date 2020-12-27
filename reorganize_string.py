from collections import Counter
def ReorganizeString(S):
    if not S or len(S) == 1:
        return S
    
    N = len(S)
    
    A = []
    for x, c in sorted(Counter(S).items(), key=lambda l: l[1]):
        if c > (N+1)/2:
            return ''
        A.extend(x*c)
        
    res = ['']*N

    res[::2] = A[N//2:]
    res[1::2] = A[:N//2]
    return ''.join(res)

a = 'abbbc'
print (ReorganizeString(a))
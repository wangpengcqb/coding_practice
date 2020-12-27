def generateMatrix(m, n):
    
    def gencor(r1, c1, r2, c2):
        if r1 == r2 and c1 == c2:
            yield r1, c1
        else:
            for i in range(c1, c2+1):
                yield r1, i
            for i in range(r1+1, r2+1):
                yield i, c2
            if r2 > r1:
                for i in range(c2-1, c1-1, -1):
                    yield r2, i
            if c2 > c1:
                for i in range(r2-1, r1, -1):
                    yield i, c1
            
        
    res = [[0 for i in range(n)] for j in range(m)]
    num = 1
    i = 0
    while i <= m-1-i and i <= n-1-i:
        r1, c1 = i, i
        r2, c2 = m-1-i, n-1-i
        for r, c in gencor(r1,c1, r2, c2):
            res[r][c] = num
            num += 1
        i += 1
    return res
    
print(generateMatrix(4,3))

print(generateMatrix(7,4))
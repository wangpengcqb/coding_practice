def isRamanujannumber(n):
    if n <= 0:
        return False
    
    lo = 1     
    hi = int(n**(1/3))+1
    count = 0
    
    while lo < hi:
        val = lo**3 + hi**3
        if val == n:
            count += 1
            if count == 2:
                return True
        elif val < n:
            lo += 1
        else:
            hi -= 1
            
    return False

n = 1729
print (isRamanujannumber(n))

n = 3512808
print (isRamanujannumber(n))

n = 4673089
print (isRamanujannumber(n))
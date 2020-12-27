def square_root(n):
    if n in [0.0,1.0]:
        return n
    if n < 0:
        return -1
        
    left = 1.0 if n > 1.0 else n
    right = n if n > 1.0 else 1.0
    
    tolerance = 1e-6
    
    error = 1.0
    
    while error >= tolerance:
        
        mid = (left + right)/2.0
        if mid * mid < n:
            left = mid
        else:
            right = mid
           
        error = abs(n - mid*mid)    
    
    return mid

n = 15.0
print(square_root(n))

n = 4.0
print(square_root(n))

n = 0.04
print(square_root(n))

n = 0.1
print(square_root(n))
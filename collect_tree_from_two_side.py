def solution(A, K, L):
    if not A or K < 0 or L < 0 or K + L > len(A):
        return -1
    N = len(A)
        
    dpleft = [0 for i in range(N)]
    dpright = [0 for i in range(N)]
    
    presum = 0
    for i in range(K):
        presum += A[i]
    
    dpleft[K-1] = presum
    left = 0
    for i in range(K, N):
        presum = presum + A[i] - A[left]
        dpleft[i] = max(dpleft[i-1], presum)
        left += 1
        
    presum = 0
    for i in range(N-1, N-L-1,-1):
        presum += A[i]
    
    dpright[N-L] = presum
    right = N-1
    for i in range(N-L-1, -1, -1):
        presum = presum + A[i] - A[right]
        dpright[i] = max(dpright[i+1], presum)
        right -= 1
    
    res = 0    
    for i in range(K-1, N-L):
        res = max(res, dpleft[i]+dpright[i])
        
    return res


A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2
print (solution(A, K, L))

A = [10, 19, 15]
K = 2
L = 2
print (solution(A, K, L))

A = [10, 19, 15]
K = 1
L = 2
print (solution(A, K, L))
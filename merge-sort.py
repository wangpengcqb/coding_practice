
def mergesort(arr):
    if not arr or len(arr) == 1:
        return arr
        
    mid = len(arr)//2    
    L = mergesort(arr[:mid])
    R = mergesort(arr[mid:])
    
    return merge(L, R)
    
    
def merge(L, R):
    i = 0
    j = 0
    index = 0
    
    res = []
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i])
            i += 1 
        else:
            res.append(R[j])
            j += 1 
            
    while i < len(L):
        res.append(L[i])
        i += 1 
    
    while j < len(R):
        res.append(R[j])
        j += 1 
        
    return res
    
    
a = [5,6,1,2,4,9,3,1,0,4,5,6,7]
b = mergesort(a) 

print(b)

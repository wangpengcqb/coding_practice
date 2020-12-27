# def binary_search(arr, last, val, equal=False):
#     lo = last + 1
#     hi = len(arr)-1
#     while lo < hi:
#         mid = (lo + hi)//2
#         if arr[mid] < val or (equal and arr[mid] == val):
#             lo = mid + 1
#         else:
#             hi = mid
#     return lo
    
def binary_search(arr, last, val, upper=False):
    lo = last + 1
    hi = len(arr)-2
    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] < val or (upper and arr[mid] == val):
            arr[mid] <= val
            lo = mid + 1
        else:
            hi = mid - 1
    return hi if upper else lo


def countSubsegments(arr):
    presum = [0]
    for a in arr:
        presum.append(presum[-1] + a)
        
    n = len(presum)
    
    cnt = 0
    for i in range(1, n-2):
        first = presum[i]
        if first > (presum[-1]/3):
            break
        
        # first index such that the sum of the second subarray is larger or equal to the sum of first subarray 
        lower_idx = binary_search(presum, i, first*2)
        # last index such that the sum of the second subarray is smaller or equal to the half of the sum of second and third subarray 
        # close interval [lower_idx, upper_idx]
        upper_idx = binary_search(presum, i, (first+presum[-1])/2, True) 
        cnt += max(upper_idx-lower_idx+1, 0)
        
    return cnt 
    
        
        
    
    
a = [1,2,2,2,5,0]
print(countSubsegments(a))

b = [1,1,3,2,5,0]
print(countSubsegments(b))

c = [1000,1000,1000]
print(countSubsegments(c))

d = [1,2,3,0,0,10,0,0]
print(countSubsegments(d))

e = [0,0,0]
print(countSubsegments(e))
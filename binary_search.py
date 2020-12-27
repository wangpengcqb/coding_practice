def binary_search(arr, val):
    lo, hi = 0, len(arr)-1
    
    while lo <= hi:
        mid = (lo + hi) //2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

arr = [1,3,5,7]
print(binary_search(arr, -1))
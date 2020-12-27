import random
import collections

def randomchoose(arr):
    if not arr:
        return -1
    presum = [0]*len(arr)
    i = 1
    while i < len(arr):
        presum[i] = presum[i-1] + arr[i-1]
        i += 1
    rand = random.random()
    i = binarysearch(presum, rand)
    return i

def binarysearch(arr, v):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi)//2
        if arr[mid] < v:
            lo = mid+1
        else:
            hi = mid
    return lo
    

a = [0.1, 0.2, 0.2, 0.3, 0.2]

cnt = collections.Counter()
for i in range(1000):
    ind = randomchoose(a)
    cnt[ind] += 1 

cnt = dict(sorted(cnt.items()))
print(list(cnt.values()))
from random import choice
def partition(arr, l, r):
    i = choice(range(l, r+1))
    
    arr[i], arr[r] = arr[r], arr[i]
    pivot = l
    for x in range(l, r):
        if arr[x] < arr[r]:
            arr[pivot], arr[x] = arr[x], arr[pivot]
            pivot += 1
            
    arr[pivot], arr[r] = arr[r], arr[pivot]
    
    return pivot
        

def quick_select(arr, k, l, r):
    if l > r:
        return -1
        
    pivot = partition(arr, l, r)

    if pivot == k - 1:
        return arr[pivot]
    elif pivot < k - 1:
        return quick_select(arr, k, pivot+1, r)
    else:
        return quick_select(arr, k, l, pivot-1)


def find_k_largest(a, k):
    if not a or len(a) < k:
        return -1

    return quick_select(a, k, 0, len(a)-1)


a = [4,7,8,14,21,1,5,9,16,12,33,28,3]
print(find_k_largest(a,3))

res = []
for i in range(len(a)):
    res.append(find_k_largest(a, i+1))
    
print(res == list(sorted(a)))
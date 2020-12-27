def reversesort(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def Permutation(arr):
    if not arr:
        return arr
    
    pivot = len(arr)-1
    
    while pivot > 0:
        if arr[pivot-1] < arr[pivot]:
            break
        pivot -= 1
    pivot -= 1
    
    if pivot == -1:
        arr.sort()
        return arr
    
    start = len(arr)-1
    while start >= pivot:
        if arr[start] > arr[pivot]:
            break
        start -= 1

    arr[pivot], arr[start] = arr[start], arr[pivot]

    reversesort(arr, pivot+1, len(arr)-1)
    
    return arr


    
def printfunction():
    print('Hello')
    
arr1 = [0, 1, 2, 5, 3, 3, 0]
arr2 = [4, 3, 2, 1]
arr3 = [1, 2, 3]
arr4 = [1,5,1]
arr5 = [1,3,2]
print(Permutation(arr5)) 
def canwin(arr, i, visited):
    if not arr:
        return False

    if i < 0 or i >= len(arr):
        return False
        
    if visited[i]:
        return False
    
    visited[i] = True    
    num = arr[i]
    
    if num == 0:
        return True
        
    return canwin(arr, i - num, visited) or canwin(arr, i + num, visited)
    
a = [3, 1, 0, 2, 5]
visited = [False for i in range(len(a))]


print (canwin(a, 4, visited))
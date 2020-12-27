def longestaverage(arr):
    if not arr:
        return -1
        
    start = end = 0
    max_len = 0
    max_ave = 0
    
    while end < len(arr):
        cur_sum = arr[end]
        while end+1 < len(arr) and arr[end] < arr[end+1]:
            end += 1
            cur_sum += arr[end]
            
        
        length = end + 1 - start
        
        if length > max_len:
            max_ave = cur_sum / length
            max_len = length
        
        end += 1
        start = end
    return max_ave
        



a = [5, 1, 2, 3, 6 , 1 ,2,3,4,5, 7,4,5]

print (longestaverage(a))
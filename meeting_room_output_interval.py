from collections import defaultdict

def findmaxoverlap(intervals):
    if not intervals:
        return []
        
    mymap = defaultdict(int)
    
    for interval in intervals:
        mymap[interval[0]] =  mymap[interval[0]] + 1 
        mymap[interval[1]] =  mymap[interval[1]] - 1
        
    
    mymap = dict(sorted(mymap.items()))
    
    start = -1
    count = 0
    max_c = 0
    store_res = False
    for k, v in mymap.items():
        count += v
        
        if count != max_c and store_res:
            res = [start, k]
        
        store_res = False
        if count > max_c:
            max_c = count
            start = k
            store_res = True
            
    return (res, max_c)
            
        
    
a = [[1,2], [4,6], [5,8],[5,10], [7,8], [7,10], [8,10], [12,13]]   
    

print(findmaxoverlap(a))
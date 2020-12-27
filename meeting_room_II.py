def getmaxmachine(query):
    if not query:
        return 0
    
    se = {}    
    for q in query:
        se[q[0]] = se.get(q[0], 0) + q[2]
        se[q[1]] = se.get(q[1], 0) - q[2]
        
    se = dict(sorted(se.items()))
    
    count = 0
    mx = 0 
    for k, v in se.items():
        count += v
        mx = max(mx, count)
        
    return mx

    
query = [[1,2,3], [1,3,1], [2,4,2], [3,5,8], [4,7,1], [5,10,6]]    


    
print (getmaxmachine(query))
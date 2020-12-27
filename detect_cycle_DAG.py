from collections import defaultdict
def detectcycle(a):
    if not a:
        return False
    
    graph = defaultdict(list)    
    for edge in a:
        graph[edge[0]].append(edge[1])
        
    visited = set()
    
    
    for edge in a:
        if edge[0] in visited:
            continue
        q = [edge[0]]
            
        while q:
            cur = q.pop(0)
            if cur in visited:
                return True
                
            visited.add(cur)
            for nei in graph[cur]:
                q.append(nei)
                
    return False

a = [[1,2], [2,3], [3,4], [5,6], [2,8], [1,7], [4,1], [3,5], [7,10], [10,7]]
b = [[1,2], [2,1]]
c = [[1,2], [2,3], [3,4]]
print(detectcycle(a))
print(detectcycle(b))
print(detectcycle(c))
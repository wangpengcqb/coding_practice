from collections import defaultdict

def bfsfind(n, graph, visited):
    
    q = [(n, -1)]
    
    while q:
        cur, parent = q.pop(0)
        visited[cur] = True
        
        for nei in graph[cur]:
            if visited[nei] and nei != parent:
                return False
            q.append((nei, cur))
            
    return True
    
def dfsfind(n, graph, visited, parent):
    visited[n] = True
    
    for nei in graph[n]:
        if not visited[nei]:
            if dfsfind(nei, graph, visited, n):
                return True
        elif nei != parent:
            return False
            
    return False
    



    
def checkcyclic(nodes, edges):
    
    visited = [False for i in range(len(nodes))]
    
    graph = defaultdict(list)
    
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    
    for n in nodes:
        if not visited[n]:
            cy = bfsfind(n, graph, visited)
            if cy:
                return False
        
    return True
 

print("Hello World")
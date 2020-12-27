from collections import defaultdict
def findNodesWithZeroAndOneParents(parentChildPairs):
    
    node = set()
    indegree = defaultdict(int)
    for p in parentChildPairs:
        node.add(p[0])
        node.add(p[1])
        indegree[p[1]] += 1
    
    zero = []
    one = []
    
    for n in node:
        if indegree[n] == 1:
            one.append(n)
        elif indegree[n] == 0:
            zero.append(n)
      
    return (zero, one)


parentChildPairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10)]
print(findNodesWithZeroAndOneParents(parentChildPairs))





def hasCommonAncestor(parentChildPairs, p1, p2):
    
    parent = defaultdict(list)
    for p in parentChildPairs:
        parent[p[1]].append(p[0])
        
    visited = set()

    q = parent[p1] + parent[p2]
    while q:
        cur = q.pop(0)
        if cur in visited:
            return True
        visited.add(cur)
        for p in parent[cur]:
            q.append(p)
    
    return False


parentChildPairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10)]
print(hasCommonAncestor(parentChildPairs, 3, 8))
print(hasCommonAncestor(parentChildPairs, 5, 8))
print(hasCommonAncestor(parentChildPairs, 6, 8))
print(hasCommonAncestor(parentChildPairs, 1, 3))


def findEarliestAncestor(parentChildPairs, p):
    
    parent = defaultdict(list)
    for par in parentChildPairs:
        parent[par[1]].append(par[0])    

    earliest = -1
    q = parent[p]

    while q:
        
        cur = q.pop(0)
        earliest = cur
        for par in parent[cur]:
            q.append(par)
            
    return earliest


parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10), (11, 2)]
print(findEarliestAncestor(parent_child_pairs, 8))
print(findEarliestAncestor(parent_child_pairs, 7))
print(findEarliestAncestor(parent_child_pairs, 6))
print(findEarliestAncestor(parent_child_pairs, 1))
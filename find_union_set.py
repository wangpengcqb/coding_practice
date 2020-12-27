from collections import defaultdict

parent = dict()
children = defaultdict(list)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        if int(px[1:]) < int(py[1:]):
            parent[y] = px
            children[px].append(y)
        else:
            parent[x] = py
            children[py].append(x)
    return 

def process(sets):
    for s in sets:
        if s[0] not in parent.keys():
            parent[s[0]] = s[0]
        if s[1] not in parent.keys():
            parent[s[1]] = s[1]
        union(s[0], s[1])
 
    return

def find_set(wi):
    
    res = [wi] + children[wi]
    cur = wi
    while parent[cur] != cur:
        cur = parent[cur]
        res += [cur]
        res.extend(children[cur])
        
    res = set(res)
    res.discard(wi)
        
    return list(res)


a = [['w1', 'w2'], ['w7', 'w2'], ['w7', 'w9'], ['w4', 'w8'], ['w5', 'w3'], ['w6', 'w3'], ['w6', 'w10']]
process(a)
print(find_set('w1'))
print(find_set('w2'))
print(find_set('w4'))
print(find_set('w3'))
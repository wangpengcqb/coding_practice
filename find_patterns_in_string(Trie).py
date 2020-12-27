from collections import defaultdict


def findpattern(s, patterns):
    if not s or not patterns:
        return []
    
    root = TrieNode()    
    for i, p in enumerate(patterns):
        cur = root
        for c in p:
            cur = cur.child[c]
        cur.word_index = i
        
    i = 0
    res = [[] for i in range(len(patterns))]
    while i < len(s):
        cur = root
        start = i
        while start < len(s) and s[start] in cur.child.keys():
            cur = cur.child[s[start]]
            start += 1
        if cur.word_index != -1:
            res[cur.word_index].append(i)
        i += 1
        
    return res

class TrieNode():
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.word_index = -1


s = 'I love love one point three acres'
list_of_strings = ['love', 'acres', 'four']

print (findpattern(s, list_of_strings))
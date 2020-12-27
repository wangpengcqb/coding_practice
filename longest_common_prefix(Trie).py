from collections import defaultdict

def commonprefix(words):
    if not words:
        return ''
    root = TrieNode()
    max_len = 0
    res = ''
    for word in words:
        max_prefix, substring = insert(root, word)
        if max_prefix > max_len:
            max_len = max_prefix
            res = substring
    return res

def insert(root, word):
    max_prefix = 0
    res = ''
    for c in word:
        root = root.child[c]
        root.count += 1
        if root.count >= 2:
            max_prefix += 1
            res += c
    
    root.isword = True
    return (max_prefix, res)
    

class TrieNode:
    def __init__(self,):
        self.count = 0
        self.child = defaultdict(TrieNode)
        self.isword = False


a = ["bandage", "banana", "anchor", "anchovy", "bass"]

print(commonprefix(a))
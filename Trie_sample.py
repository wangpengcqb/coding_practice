class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = None



root = TrieNode()


def addword(word):
    cur = root
    for c in word:
        if c not in cur.child.keys():
            cur.child[c] =  TrieNode()
        cur = cur.child[c]
    cur.word = word

def searchword(word):
    cur = root
    for c in word:
        if c not in cur.child.keys():
            return False
        cur = cur.child[c]
    
    return cur.word is not None
    
addword('test')
addword('myword')
addword('text')


        

print(searchword('mytest'))
print(searchword('test'))
print(searchword('text'))
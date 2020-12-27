class Iterator:
    def __init__(self, root):
        self.stack = []
        self.push_all(root)
    
    def push_all(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        return
    
    def next_node(self):
        if not self.stack:
            return None 
        else:
            cur = self.stack.pop()
            if cur.right:
                self.push_all(cur.right)
            return cur
            
    def next_leaf(self):
        cur = self.next_node()
        if not cur:
            return cur
            
        while cur.left or cur.right:
            cur = self.next_node()
            
        return cur.val
        

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None      
        
        
        
root = TreeNode('')
lchild = TreeNode('this')
rchild = TreeNode('empty')
root.left = lchild
root.right = rchild
lchild.left = TreeNode('a')
lchild.right = TreeNode('bcd')
rchild.left = TreeNode('ef')
rchild.right = TreeNode('gg')

it = Iterator(root)

print(it.next_leaf())
print(it.next_leaf())
print(it.next_leaf())
print(it.next_leaf())
print(it.next_leaf())
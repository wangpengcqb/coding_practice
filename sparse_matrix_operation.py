from collections import defaultdict
class sparsematrix:
    def __init__(self):
        self.matrix = defaultdict(dict)

    def set(self, i, j, v):
        self.matrix[i][j] = v
        return True
        
    def get(self, i, j):
        b = self.matrix[i]
        if j not in b:
            return 0
        return b[j]
        
    def add(self, m2):
        res = sparsematrix()
        for i, row in self.matrix.items():
            for j, val in row.items():
                res.set(i, j, val + m2.get(i,j))
                
        for i, row in m2.matrix.items():
            for j, val in row.items():
                res.set(i, j, val + self.get(i,j))
                
        return res
        
    def multiply(self, m2):
        res = sparsematrix()
        for i in self.matrix:
            for k in self.matrix[i]:
                if k not in m2.matrix: continue
                for j in m2.matrix[k]:
                    val = res.get(i, j)
                    res.set(i, j, val + self.get(i,k) * m2.get(k,j))
                    
        return res
        

m1 = sparsematrix()
m1.set(0,0,4)
m1.set(0,2,1)
m1.set(1,2,2)

m2 = sparsematrix()
m2.set(0,1,3)
m2.set(1,0,5)
m2.set(1,2,4)

m3 = m1.add(m2)
print(m3.matrix)

m4 = sparsematrix()
m4.set(0,0,1)
m4.set(1,0,7)

m5 = sparsematrix()
m5.set(0,0,2)
m5.set(1,1,3)

m6 = m4.multiply(m5)
print(m6.matrix)

m7 = sparsematrix()
m7.set(0,0,1)
m7.set(0,1,2)
m7.set(1,0,3)
m7.set(1,1,4)

m8 = sparsematrix()
m8.set(0,0,5)
m8.set(0,1,6)
m8.set(1,0,7)
m8.set(1,1,8)

m9 = m7.multiply(m8)
print(m9.matrix)
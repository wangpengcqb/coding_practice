def find_rect(island):
    
    def findtl(island):
        for i in range(len(island)):
            for j in range(len(island[0])):
                if island[i][j] == 0:
                    tlr = i
                    tlc = j
                    return (tlr, tlc)
        return (-1, -1)
        
    tlr, tlc = findtl(island)
    
    if (tlr, tlc) == (-1, -1):
        return []
        
    i, j = tlr, tlc
    while i+1 < len(island) and island[i+1][j] == 0:
        i += 1
    while j+1 < len(island[0]) and island[i][j+1] == 0:
        j += 1
    
    return [(tlr, tlc), (i,j)]

island = [
[1,1,1,1,1,1],
[1,0,0,0,1,1],
[1,0,0,0,1,1],
[1,0,0,0,1,1],
[1,1,1,1,1,1]
]

print (find_rect(island))


def find_rects(island):
    
    def findtl(island):
        for i in range(len(island)):
            for j in range(len(island[0])):
                if island[i][j] == 0:
                    tlr = i
                    tlc = j
                    return (tlr, tlc)
        return (-1, -1)
    
    res = []   
    while True:
        tlr, tlc = findtl(island)
        
        if (tlr, tlc) == (-1, -1):
            return res
        
        i = tlr
        j = tlc
        while i < len(island) and island[i][tlc] == 0:
            j = tlc
            while j < len(island[0]) and island[i][j] == 0:
                island[i][j] = 1
                j += 1
            i += 1
        res.append((tlr, tlc, i-1, j-1))
    
    return res

island = [
[1,1,1,1,1,1],
[1,0,1,0,1,1],
[1,0,1,0,1,0],
[1,0,1,1,1,1],
[1,1,1,1,1,0]
]

print (find_rects(island))



def find_shapes(island):
    
    def dfs(island, i, j, cor):
        
        island[i][j] = 1
        cor.append((i,j))
        
        di = [(0,1), (1,0), (0,-1), (-1, 0)]
        for dx, dy in di:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < len(island) and 0 <= ny < len(island[0]) and island[nx][ny] == 0:
                dfs(island, nx, ny, cor)
        return
    
    
    res = []
    for i in range(len(island)):
        for j in range(len(island[0])):
            if island[i][j] == 0:
                cor = []
                dfs(island, i, j, cor)
                res.append(cor)
    
    return res

island = [
[1,1,1,1,0,0],
[1,0,1,0,1,0],
[1,0,1,0,1,0],
[1,0,0,0,1,1],
[1,1,1,1,1,0]
]

print(find_shapes(island))
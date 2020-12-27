def spiral_matrix(matrix):
    
    m = len(matrix)
    n = len(matrix[0])
    
    max_l = min(m//2, n//2)
    presum = [0 for i in range(max_l+1)]
    for l in range(1, max_l+1):
        presum[l] = presum[l-1] + 2*(m-1-2*(l-1)) + 2*(n-1-2*(l-1))

    
    res = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            l = min(i, j, m-1-i, n-1-j)
            if l == i:
                rank = presum[l] + j - l
            elif l == n-1-j:
                rank = presum[l] + n-1-2*l + i-l    
            elif l == m-1-i:
                rank = presum[l] + n-1-2*l + m-1-2*l + n-1-l-j
            elif l == j:
                rank = presum[l] + m-1-2*l + n-1-2*l + m-1-2*l + n-1-l-i

            x, y = rank//n, rank%n
            res[x][y] = matrix[i][j]
    return res



matrix1 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print(spiral_matrix(matrix1))


matrix2 = [
[1,2,3,4,5,6,7,8,9,10],
[11,12,13,14,15,16,17,18,19,20],
[21,22,23,24,25,26,27,28,29,30],
[31,32,33,34,35,36,37,38,39,40],    
]

print(spiral_matrix(matrix2))


matrix3 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [10,11,12 ],
]

print(spiral_matrix(matrix3))


matrix4 = [[1,2,3,4]]
print(spiral_matrix(matrix4))


matrix5 = [[1],[2],[3],[4]]

print(spiral_matrix(matrix5))


matrix6 = [[1,2],[3,4],[5,6],[7,8], [9,10], [11,12], [13,14], [15,16], [17,18], [19,20]]

print(spiral_matrix(matrix6))
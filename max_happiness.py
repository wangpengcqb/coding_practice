h_map = {
    'c':4,
    'w':3,
    'm':2,
    's':1
}

def calculate_happiness(s):
    res = 0
    for c in s:
        res += h_map[c]
    
    return res*len(s)


def find_max_happiness(p, n):
    if not p or not n:
        return 0
        
    m = len(p)
    dp = [[0 for i in range(n+1)] for j in range(m)]
    
    for i in range(m):
        for j in range(n+1):
            each = p[i]
            if j >= len(each):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-len(each)] + calculate_happiness(each))
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp)
    res = 0
    for e in dp[m-1]:
        res = max(res, e)
        
    return res


p = ['msc', 'wmc', 'wwmcs', 'ssmmc']
n = 8
print (find_max_happiness(p, n))
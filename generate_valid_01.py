def backtrack(res, n, temp):
    if len(temp) == n:
        res.append(temp)
        return
        
    for c in ['0', '1']:
        if len(temp) >= 2 and temp[-1] == c and temp[-2] == c:
            continue
        backtrack(res, n, temp+c)
    
    return

def generate_string(n):
    if n == 0:
        return ''
        
    res = []
    backtrack(res, n, '')
    
    return res
    
n = 3
print(generate_string(n))

n = 5
print(generate_string(n))
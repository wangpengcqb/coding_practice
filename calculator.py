def calculator(s):
    if not s:
        return 0
        
    res = 0
    op = '+'
    stack = []
    
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if op == '+':
                res += int(s[i])
            elif op == '*':
                res *= int(s[i])
        elif s[i] == '+':
            op = '+'
        elif s[i] == '*':
            op = '*'
        elif s[i] == '(':
            stack.append(res)
            stack.append(op)
            res = 0
            op = '+'
        elif s[i] == ')':
            op = stack.pop()
            pre = stack.pop()
            if op == '+':
                res = pre + res
            elif op == '*':
                res = pre*res
        i += 1
        
    return res
    


a = '((1+2)*((1+((2)))*3))'
b = '(((4)))'
c = '(1+(2*3))'
d = '((1+2)*3)'

print (calculator(a))
print (calculator(b))
print (calculator(c))
print (calculator(d))
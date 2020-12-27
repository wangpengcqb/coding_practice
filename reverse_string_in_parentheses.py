def reverse_string(s):
    if not s or len(s) <= 1:
        return s
        
    stack = []
    i = 0
    res = ''
    while i < len(s):
        if s[i].isalpha():
            res += s[i]
        elif s[i] == '(':
            stack.append(res)
            res = ''
        elif s[i] == ')':
            res = stack.pop() + res[::-1]
        i += 1

    return res


s1 = "ab()"
s2 = "ab(cd)"
s3 = "ab(cd(ef))"
s4 = "ab(cd(ef)(gh)(hi(jk(lm))))"

print(reverse_string(s1))
print(reverse_string(s2))
print(reverse_string(s3))
print(reverse_string(s4))
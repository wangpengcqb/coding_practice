def nestprint(s):
    if not s:
        return
    
    indent = start = end = 0
    
    while end < len(s):
        if s[end] in ['(', ')']:
            subs = s[start:end].split(' ')
            for sub in subs:
                if len(sub) > 0:
                    print(' '*indent + sub)
            
            if s[end] == '(':
                print(' '*indent + s[end])
                indent += 4
            elif s[end] == ')':
                indent -= 4
                print(' '*indent + s[end])
            end += 1
            start = end
        else:
            end += 1 

a = '(Hi Hello(Hey(yoyo ) ) Bob)'
b = '(ab(cd))(ef)'
c = '(hot dog(hello word!(you) here))'
nestprint(c)
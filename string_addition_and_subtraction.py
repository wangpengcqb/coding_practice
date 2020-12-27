"""
'123', '224' --> '347'
'123', '224' --> '-101'
"""

def addition(s1, s2):
    if not s1 or not s2:
        return s1 if s1 else s2
    
    i = len(s1)-1
    j = len(s2)-1
    
    carry = 0
    res = ''
    while i >= 0 or j >= 0 or carry > 0:
        num1 = int(s1[i]) if i >= 0 else 0
        num2 = int(s2[j]) if j >= 0 else 0
        sm = num1 + num2 + carry
        res = str(sm%10) + res
        carry = sm//10
        i -= 1
        j -= 1
        
    return res
        
# s1 = '123'
# s2 = '224'
# print(addition(s1, s2))   

# s1 = '234'
# s2 = '0'
# print(addition(s1, s2)) 



def larger(s1, s2):
    if len(s1) > len(s2):
        return True
    elif len(s1) < len(s2):
        return False
    else:
        i = 0
        while i < len(s1):
            diff = int(s1[i]) - int(s2[i])
            if diff > 0:
                return True
            elif diff < 0:
                return False
            i += 1
    return True
    
        
def subtract(s1, s2):
    if not s1 and not s2:
        return ''
    if not s1:
        return '-' + s2
    if not s2:
        return s1
    
    res = ''
    neg = False
    le = larger(s1, s2) 
    if not le:
        neg = True
        s1, s2 = s2, s1
    
    carry = 0
    i = len(s1)-1
    j = len(s2)-1
    
    while i >= 0 or j >= 0 or carry:
        num1 = int(s1[i]) if i >= 0 else 0
        num2 = int(s2[j]) if j >= 0 else 0
        diff = num1 - num2 - carry
        if diff < 0:
            diff += 10
            carry = 1
        else:
            carry = 0
        res = str(diff) + res
        i -= 1
        j -= 1        
    
    res = res.lstrip('0')
    return '-' + res if neg else res

s1 = '35'
s2 = '678'
print(subtract(s1, s2)) 
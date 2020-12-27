phone = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}

def decode_phone_number(s):
    if len(s) == 1:
        return phone[int(s)][0]
        
    start = end = 0
    
    res = ''
    while end < len(s):
        while end < len(s) and s[end] == s[start] and s[end] != '*':
            end += 1
        cnt = end - start
        res += phone[int(s[start])][cnt-1]
        
        if end < len(s) and s[end] == '*':
            end += 1
        
        start = end
        
    return res
    


a = "222449333"
b = "222*22*223*3334"
print(decode_phone_number(a))
print(decode_phone_number(b))
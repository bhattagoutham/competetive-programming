# Complete the superReducedString function below.
# def superReducedString(s):
#     s = list(s); i=1
    
#     while i < len(s):
        
#         if s[i] == s[i-1]:
#             del s[i]; del s[i-1]
#             # after deletion check back
#             if i > 1:
#                 i -= 1
#         else:
#             i += 1
#     return ''.join(s) if s else 'Empty String'

# s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# print(superReducedString(s))


# find largest alternate string
def make_from_s(s, a, b):
    return ''.join([x for x in s if x in [a, b]])

def isalt(s):
    i = 2; n = len(s); isalt = True
    patt = s[0:2]
    
    if n == 1:
        return False
    
    odd = True if not n % 2 == 0 else False
    n = n-1 if odd else n

    while i < n:
        if not s[i:i+2] == patt:
            isalt = False; break
        i += 2
    isalt = False if isalt and odd and s[-1] != s[0] else isalt
    return isalt


# Complete the alternate function below.
def alternate(s):
    
    char_set = []
    [char_set.append(x) for x in s if x not in char_set]
    i = 1; max_len = 0
    n = len(char_set)
    for i in range(n):
        for j in range(i+1, n):
            temp = make_from_s(s, char_set[i], char_set[j])
            print(char_set[i], char_set[j])
            print(temp, isalt(temp), len(temp))
            if isalt(temp) and max_len < len(temp):
                max_len = len(temp)
    return max_len


            

    

print(alternate('asdcbsdcagfsdbgdfanfghbsfdab'))

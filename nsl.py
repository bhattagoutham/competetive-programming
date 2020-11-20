import stackds as st

input_arr = [43, 34, 51, 92, 11, 63, 34, 12]

# nearest greatest to left
def ngl():
    leftmost_idx = -1
    ngl_value = []
    ngl_idx = []
    stk = st.Stack(max_size=None, fixed=False)

    for i in range(len(input_arr)):
        while(not stk.isEmpty() and input_arr[i] > stk.top()[0]):
            stk.pop()
        if stk.isEmpty():
            ngl_idx.append(leftmost_idx)
        else:
            ngl_idx.append(stk.top()[1])

        stk.push((input_arr[i], i))
            
    return ngl_idx

# nearest greates to right
def ngr():
    n = len(input_arr)
    rightmost_idx = n
    ngr_idx = []
    stk = st.Stack(max_size=None, fixed=False)
    res = st.Stack(max_size=None, fixed=False)

    for i in range(n):
        while(not stk.isEmpty() and stk.top()[0] < input_arr[n-i-1]):
            stk.pop()
        if stk.isEmpty():
            res.push(rightmost_idx)
        else:
            res.push(stk.top()[1])
        stk.push((input_arr[n-i-1], n-i-1))
    
    while(not res.isEmpty()):
        ngr_idx.append(res.pop())
    return ngr_idx

def stock_span():
    res = []
    for i, ngL in enumerate(ngl()):
        res.append(i-ngL-1)
    return res

# test cases
if __name__ == '__main__':
    print(ngl())
    print(ngr())
    print(stock_span())

    
    
     



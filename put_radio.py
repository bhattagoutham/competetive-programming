def hackerlandRadioTransmitters(x, k):
    
    x.sort()
    # print(x[0:300])
    i = 0; put_radio = True; cnt = 0; strt = 0; n = len(x)
    print(x[strt])
    while i < n:
        while i < n and x[i] - x[strt] < k:
            i += 1
        
        if i >= n:
            if put_radio:
                cnt += 1; print('R:', x[i-1])
            break
            
        if put_radio:
            strt = i-1 if x[i] - x[strt] > k else i
            cnt += 1; put_radio = False; print('R:', x[strt])
        else:
            strt = i if x[i] - x[strt] > k else i+1 
            put_radio = True; print('S:', x[strt])
        
    return cnt

# x = [7, 2, 4, 6, 5, 9, 12, 11]
# k = 2
n = 0; k = 0; x = []
with open('inp13', 'r') as f:
    s1 = f.readline()
    s2 = f.readline()
    # print(s1, s2)
    n, k = map(int, s1.split())
    x = list(map(int, s2.split()))
    
print(hackerlandRadioTransmitters(x, k))
print(x[-80:])

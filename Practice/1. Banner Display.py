from collections import Counter as di

def solve():
    n = int(input())
    s = input()
    st = set('coderams')
    
    d = di(s)
    
    cnt = 0
    
    while True:
        for i in st:
            if d[i] == 0:
                return cnt
            else:
                d[i] -= 1
        cnt += 1
        
        
print(solve())
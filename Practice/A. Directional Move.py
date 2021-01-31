def solve():
    n = int(input())
    s = input()
    ret = 'E'
    l = ['E', 'N', 'W', 'S']
    
    for i in s:
        idx = l.index(ret)
        if int(i):
            ret = l[(idx + 1) % 4]
        else:
            ret = l[(idx - 1) % 4]
        
    return ret
    
 
for i in range(int(input())):
    print(solve())
def solve():
    a, b, c = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    
    while c:
        if len(l) == 1:
            return l[0]
            
        tmp = l[-b:]
        x = b
        while x:
            l.pop()
            x -= 1
        l.append(sum(tmp))

        c -= 1
        
    return max(l)
        
        
print(solve())
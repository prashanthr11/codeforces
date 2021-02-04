def solve():
    n = int(input())
    l = list(map(int, input().split()))
    ret = list()
    i = 0
    while i < n - i:
        ret.append(l[i])
        ret.append(l[n - i - 1])
        i += 1
 
    return ret[:-1] if n % 2 else ret
 
 
for i in range(int(input())):
    print(*solve())

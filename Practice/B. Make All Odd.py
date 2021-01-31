def solve():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    
    for i in s:
        if not i % 2:
            cnt += 1
    
    return -1 if cnt == n else cnt
 
for i in range(int(input())):
    print(solve())
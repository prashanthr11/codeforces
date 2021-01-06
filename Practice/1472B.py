from collections import Counter as di


def solve():
    n = int(input())
    l = list(map(int, input().split()))
    d = di(l)
    sumi = sum(l)

    if sumi % 2 or d[i] % 2:
        return False

    sumi //= 2

    if sumi % 2 == 0 or (sumi % 2 == 1 and d[1] >= 1):
        return True
    return False


for i in range(int(input())):
    print('YES') if solve() else print('NO')
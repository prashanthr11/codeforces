def solve():
    a, b, c = map(int, input().split())
    if c == 1:
        return True

    cnt = 1
    while True:
        if cnt >= c or (a % 2 and b % 2):
            break

        else:
            if a % 2 == 0:
                a //= 2
            else:
                b //= 2
            cnt *= 2

    return True if cnt >= c else False


for i in range(int(input())):
    print('YES') if solve() else print('NO')
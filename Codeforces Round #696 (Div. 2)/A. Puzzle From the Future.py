def solve():
    s = int(input())
    a = input()
    ret = '1'

    for i in range(1, len(a)):
        if a[i] == '0':
            if a[i - 1] == '1':
                if ret[-1] == '1':
                    ret += '1'
                else:
                    ret += '0'
            else:
                if ret[-1] == '0':
                    ret += '1'
                else:
                    ret += '0'
        else:
            if a[i - 1] == '1':
                if ret[-1] == '1':
                    ret += '0'
                else:
                    ret += '1'
            else:
                if ret[-1] == '0':
                    ret += '1'
                else:
                    ret += '1'

    return ret


for i in range(int(input())):
    print(solve())

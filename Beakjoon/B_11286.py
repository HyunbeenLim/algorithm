import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    order = int(input())
    if order:
        arr.append()
    else:
        if arr:
            min_abs = 10
            for num in arr:
                if abs(num) <= min_abs:
                    min_abs = num
            print(min_abs)
        else:
            print(0)

# 런타임 에러
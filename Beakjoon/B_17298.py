import sys
input = sys.stdin.readline

N = int(input())

number_list = list(map(int, input().split()))
ans = []

for i in range(N - 1):
    num = number_list[i]
    rest = number_list[(i + 1):]
    right_big = -1

    for right_num in rest:
        if right_num > right_big:
            right_big = right_num
    
    ans.append(right_big)
ans.append(-1)

for answer in ans:
    print(answer, end = ' ')


# 시간 초과

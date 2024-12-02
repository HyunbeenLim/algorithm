import sys
sys.stdin = open('./sample_input.txt', 'r')

N = int(input())

lst = []

for _ in range(N):
    lst.append(list(input().split()))

for i in range(N - 1, 0, -1):
    for j in range(i):
        if int(lst[j][1]) > int(lst[j + 1][1]):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        elif lst[j][1] == lst[j + 1][1]:
            if lst[j][0][0] > lst[j + 1][0][0]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

for i in range(N):
    print(lst[i][0])
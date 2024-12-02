import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

number_list = list(map(int, input().split()))

i = 0
j = n - 1
number_list.sort()
cnt = 0

while i < j:
    sum_value = number_list[i] + number_list[j]
    if sum_value == m:
        cnt += 1
        i += 1
        j -= 1
    elif sum_value > m:
        j -= 1
    else:
        i += 1

print(cnt)
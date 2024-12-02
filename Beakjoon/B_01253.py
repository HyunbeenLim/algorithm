## 내가 짠 코드 - 계속 틀리는데 왜 틀리는지 모르겠음

import sys
input = sys.stdin.readline

n = int(input())
number_list = list(map(int, input().split()))
number_list.sort()

cnt = 0

for k in range(2, n):
    number_to_find = number_list[k]
    i = 0
    j = k - 1

    while i < j:
        sum_value = number_list[i] + number_list[j]
        if sum_value == number_to_find:
            cnt += 1
            break
        elif sum_value > number_to_find:
            j -= 1
        else:
            i += 1

print(cnt)

## 교재 참고 코드

import sys
input = sys.stdin.readline

n = int(input())
number_list = list(map(int, input().split()))
number_list.sort()

cnt = 0

for k in range(n):
    number_to_find = number_list[k]
    i = 0
    j = n - 1
    
    while i < j:
        sum_value = number_list[i] + number_list[j]
        if sum_value == number_to_find:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif sum_value > number_to_find:
            j -= 1
        else:
            i += 1

print(cnt)
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

numbers = list(map(int, input().split()))

if numbers[0] == 1:
    flag = 'ascending'
    idx = 0
    while idx < 8:
        if idx+1 != numbers[idx]:
            flag = 'mixed'
            break
        idx += 1
    print(flag)
elif numbers[0] == 8:
    flag = 'descending'
    idx = 0
    while idx < 8:
        if numbers[idx] != (8 - idx % 8):
            flag = 'mixed'
            break
        idx += 1
    print(flag)
else:
    print('mixed')
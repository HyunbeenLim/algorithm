import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))

cnt = 0

for number in numbers:
    if number == 1:
        continue
    else:
        cur_num = 2
        while cur_num < (number // 2 + 1):
            if number % cur_num == 0:
                break
            cur_num += 1
        else:
            cnt += 1

print(cnt)
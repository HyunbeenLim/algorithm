import sys
input = sys.stdin.readline
n = int(input())

cnt = 1 # end_idx가 n이 아닐 때까지 반복하기 때문
sum_value = 1

start_idx = 1
end_idx = 1

while end_idx != n:
    if sum_value == n:
        cnt += 1
        end_idx += 1
        sum_value += end_idx
    elif sum_value < n:
        end_idx += 1
        sum_value += end_idx
    else:
        sum_value -= start_idx
        start_idx += 1

print(cnt)
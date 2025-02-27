import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start, end = 0, N-1
min_sum = 2e9 + 1

while start < end:
    liquid_1, liquid_2 = liquid[start], liquid[end]
    current_sum = liquid_1 + liquid_2

    if min_sum > abs(current_sum):
        min_sum = abs(current_sum)
        best_combi = [liquid_1, liquid_2]
    
    if current_sum == 0:
        break
    elif current_sum > 0:
        end -= 1
    else:
        start += 1

print(*best_combi)
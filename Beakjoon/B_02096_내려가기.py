import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())
a, b, c = map(int, input().split())
prev_max = [a, b, c]
prev_min = [a, b, c]

for _ in range(N-1):
    new_a, new_b, new_c = map(int, input().split())

    curr_max = [max(prev_max[0], prev_max[1]) + new_a,
                max(prev_max[0], prev_max[1], prev_max[2]) + new_b,
                max(prev_max[1], prev_max[2]) + new_c]
    
    curr_min = [min(prev_min[0], prev_min[1]) + new_a,
                min(prev_min[0], prev_min[1], prev_min[2]) + new_b,
                min(prev_min[1], prev_min[2]) + new_c]
    
    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))

## 메모리 초과
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# # dp[r][c][0]: 최댓값, dp[r][c][1]: 최솟값
# dp = [[[float('-inf'), float('inf')] for _ in range(3)] for _ in range(N)]

# for c in range(3):
#     dp[0][c][0] = board[0][c]
#     dp[0][c][1] = board[0][c]

# for r in range(1, N):
#     for c in range(3):
#         for k in [-1, 0, 1]:
#             prev_c = c - k
#             if 0 <= prev_c < 3:
#                 dp[r][c][0] = max(dp[r][c][0], dp[r-1][prev_c][0] + board[r][c])
#                 dp[r][c][1] = min(dp[r][c][1], dp[r-1][prev_c][1] + board[r][c])

# min_val = float('inf')
# max_val = float('-inf')
# for ele in dp[N-1]:
#     if max_val < ele[0]:
#         max_val = ele[0]
#     if min_val > ele[1]:
#         min_val = ele[1]

# print(max_val, min_val)
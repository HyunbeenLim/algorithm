import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

dp = [0] * (N + 1)
dp[1:4] = [1, 2, 3]

for i in range(4, N+1):
    dp[i] = i
    j = 1

    while j ** 2 <= i:
        dp[i] = min(dp[i], dp[i - j**2] + 1)
        j += 1

print(dp[N])
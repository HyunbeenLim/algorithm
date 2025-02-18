import sys
input = sys.stdin.readline

N, K = map(int, input().split())

worth = []

for _ in range(N):
    worth.append(int(input()))

dp = [0] * (K + 1)
dp[0] = 1

for coin in worth:
    for j in range(coin, K + 1):
        dp[j] += dp[j-coin]

print(dp[K])
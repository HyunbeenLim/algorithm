import sys
input = sys.stdin.readline

N = int(input())

maze = list(map(int, input().split()))
dp = [0] + [1000000] * (N - 1)

for i in range(N):
    for j in range(i):
        if maze[j] >= i-j:
            dp[i] = min(dp[i], dp[j]+1)

if dp[N-1] > 10000:
    print(-1)
else:
    print(dp[N-1])
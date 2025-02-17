import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')


N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
min_cost = 1000 * 1000 + 1

for c in range(3):
    dp = [[1000 * 1000 + 1] * 3 for _ in range(N)]
    dp[0][c] = rgb[0][c]
    for i in range(1, N-1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
    
    for last in range(3):
        if last != c:
            dp[N-1][last] = min(dp[N-2][(last-1)%3], dp[N-2][(last+1)%3]) + rgb[N-1][last]

    min_cost = min(min_cost, min(dp[N-1]))

print(min_cost)

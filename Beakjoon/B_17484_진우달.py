import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

# 좌하, 하, 우하
dc = [-1, 0, 1]

N, M = map(int, input().split())

cost = [list(map(int, input().split())) for _ in range(N)]

# dp[r][c][dir] = dp[r][c-1][dir]에서 dir 방향으로 도착했을 때 최소 연료
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

for c in range(M):
    for k in range(3):
        dp[0][c][k] = cost[0][c]

for r in range(1, N):
    for c in range(M):
        for k in range(3):
            prev_col = c - dc[k]
            if 0 <= prev_col < M:
                for prev_dir in range(3):
                    # 이전과 같은 방향이면 건너뛰기
                    if prev_dir == k:
                        continue
                    dp[r][c][k] = min(dp[r][c][k], dp[r-1][prev_col][prev_dir]+cost[r][c])

ans = float('inf')
for c in range(M):
    ans = min(ans, min(dp[N-1][c]))
print(ans)
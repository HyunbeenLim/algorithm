import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

dp[0][0] = mars[0][0]

# 첫 행은 왼쪽에서 오른쪽으로만 이동 가능
for c in range(1, M):
    dp[0][c] = dp[0][c-1] + mars[0][c]

for r in range(1, N):
    # 왼쪽 -> 오른쪽
    left_dir = [float('-inf')] * M
    # 오른쪽 -> 왼쪽
    right_dir = [float('-inf')] * M

    # 왼쪽 -> 오른쪽
    ## 첫 칸은 위에서 내려오는 방법만 존재
    left_dir[0] = dp[r-1][0] + mars[r][0]
    for c in range(1, M):
        # 위에서 내려온 값과 왼쪽에서 온 값 비교 후 최댓값으로 갱신
        left_dir[c] = max(left_dir[c-1], dp[r-1][c]) + mars[r][c]
    
    # 오른쪽 -> 왼쪽
    right_dir[M-1] = dp[r-1][M-1] + mars[r][M-1]
    for c in range(M-2, -1, -1):
        right_dir[c] = max(right_dir[c+1], dp[r-1][c]) + mars[r][c]
    
    # 최종 비교
    for c in range(M):
        dp[r][c] = max(left_dir[c], right_dir[c])

print(dp[N-1][M-1])
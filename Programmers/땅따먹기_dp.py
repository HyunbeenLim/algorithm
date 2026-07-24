def solution(land):
    N = len(land)

    # n행 c열 도착 시점에서의 최대값 저장
    dp = [[0] * 4 for _ in range(N)]
    for c in range(4):
        dp[0][c] = land[0][c]

    for r in range(1, N):
        for c in range(4):
            current_max = 0
            for k in range(4):
                if k != c:
                    current_max = max(current_max, dp[r-1][k])
            dp[r][c] = land[r][c] + current_max

    return max(dp[N-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
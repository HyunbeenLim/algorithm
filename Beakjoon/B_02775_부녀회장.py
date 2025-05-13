import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    dp = [[0] * (N+1) for _ in range(K+1)]
    
    # 0층 완성
    for i in range(N+1):
        dp[0][i] = i
    
    for k in range(1, K+1):
        for n in range(1, N+1):
            for j in range(1, n+1):
                dp[k][n] += dp[k-1][j]
    
    print(dp[K][N])
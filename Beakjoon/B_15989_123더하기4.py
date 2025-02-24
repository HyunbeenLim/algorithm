import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):
    N = int(input())

    dp = [0] * (N + 1)

    dp[1] = 1

    if N >= 2:
        dp[2] = 2

    if N >= 3:
        dp[3] = 3

    # 노가다 결과물
    for i in range(4, N+1):
        dp[i] = dp[i-3] + i//2 + 1

    print(dp[N])
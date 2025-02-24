import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

dp = [[0] for _ in range(N+1)]

# 1, 2, 3까지는 직접 넣어주기
dp[1].append('1')

if N >= 2:
    dp[2].append('1+1')
    dp[2].append('2')

if N >= 3:
    dp[3].append('1+1+1')
    dp[3].append('1+2')
    dp[3].append('2+1')
    dp[3].append('3')

for i in range(4, N+1):
    # N을 만드는 방법 중 1, 2, 3이 맨 앞에 오는 방법들 사전 순 정렬
    for j in range(1, len(dp[i-1])):
        dp[i].append('1+'+dp[i-1][j])

    for j in range(1, len(dp[i-2])):
        dp[i].append('2+'+dp[i-2][j])

    for j in range(1, len(dp[i-3])):
        dp[i].append('3+'+dp[i-3][j])

if K >= len(dp[N]):
    print(-1)
else:
    print(dp[N][K])
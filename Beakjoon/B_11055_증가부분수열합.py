import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def largest():
    dp = [0] * N

    for i in range(N):
        dp[i] = numbers[i]
    
    for i in range(N):
        for j in range(i):
            # 수열에 포함할 수 있다면
            if numbers[j] < numbers[i]:
                # 이전 최댓값에 자기 자신을 더해준다
                dp[i] = max(dp[i], dp[j]+numbers[i])

    return max(dp)

N = int(input())
numbers = list(map(int, input().split()))

ans = largest()

print(ans)
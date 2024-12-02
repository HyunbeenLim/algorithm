import sys
sys.stdin = open('./sample_input.txt', 'r')


####### 백트래킹 시간초과 #######
def knapsack(idx, volume, value):
    global max_value

    if volume > K:
        return
    
    if value > max_value:
        max_value = value

    if idx == N:
        return
    
    # 더하거나 더하지 않거나
    knapsack(idx + 1, volume + V[idx], value + C[idx])
    knapsack(idx + 1, volume, value)

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    
    V = [0]   # 부피
    C = [0]   # 가치
    
    for _ in range(N):
        v_i, c_i = map(int, input().split())
        V.append(v_i)
        C.append(c_i)
    
    max_value = 0
    
    knapsack(0, 0, 0)

    print(f'#{tc} {max_value}')


####### 블로그 dp 코드 #######
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    V = []
    C = []
    dp = [[0] * (K + 1) for _ in range(N+1)]
    for i in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c) # 입력받기

    for i in range(1, N+1): # 물건 선택
        for k in range(1, K+1): # 가방의 크기 K까지의 
            if k >= V[i-1]: # 가방에 물건이 들어간다면
                # dp 점화식
                dp[i][k] = max(dp[i-1][k-V[i-1]]+C[i-1], dp[i-1][k])
            else:
                # 가방에 물건이 들어가지 않는다면 
                dp[i][k] = dp[i-1][k]
    print(f'#{test_case} {dp[N][K]}') # 1부터 N까지의 물건중 K만큼의 크기를 만족시키는 가장 큰 값
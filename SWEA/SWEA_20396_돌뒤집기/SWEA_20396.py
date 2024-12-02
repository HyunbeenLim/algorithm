T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    stones = list(map(int, input().split()))
    
    for _ in range(M):
        i, j = map(int, input().split())
        
        color_i = stones[i - 1]
        
        # i-1 부터 i+j-2 까지 같은 색으로 바꿔주기
        ## i-1은 이미 그 색이라 i부터 시작
        for idx in range(i, i + j - 1):
            # N보다 작은지 확인
            if idx < N:
                stones[idx] = color_i
    
    print(f'#{tc}', *stones)
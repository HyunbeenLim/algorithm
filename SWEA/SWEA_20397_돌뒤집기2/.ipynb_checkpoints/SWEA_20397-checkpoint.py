T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    
    # i번째 돌 => 인덱스는 i - 1
    for _ in range(M):
        i, j = map(int, input().split())
        
        for neighbor in range(1, j + 1):
            if (0 <= (i - 1 - neighbor)) and ((i - 1 + neighbor) < N):
                if stones[i - 1 - neighbor] == stones[i - 1 + neighbor]:
                    if stones[i - 1 - neighbor] == 1:
                        stones[i - 1 - neighbor] = 0
                        stones[i - 1 + neighbor] = 0
                    else:
                        stones[i - 1 - neighbor] = 1
                        stones[i - 1 + neighbor] = 1
                        
    print(f'#{tc}', *stones)
    
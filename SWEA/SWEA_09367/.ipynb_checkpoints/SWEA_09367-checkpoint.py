T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    
    counts = [1] * N
    
    for i in range(N - 1):
        if carrots[i + 1] > carrots[i]:
            counts[i + 1] = counts[i] + 1
            
    print(f'#{tc} {max(counts)}')
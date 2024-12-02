T = int(input())

for tc in range(1, T + 1):
    N = 5
    max_j = 15
    
    matrix = [list(input()) for _ in range(N)]
    
    ans = ''
    for j in range(max_j):
        for i in range(N):
            if j < len(matrix[i]):
                ans += matrix[i][j]
                
    print(f'#{tc} {ans}')
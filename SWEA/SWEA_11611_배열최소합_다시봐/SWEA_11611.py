import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(n,sum) :
    global min_sum
 
    # 가지치기
    if sum >= min_sum :
        return
 
 
    if n == N :
        # 최솟값 갱신
        min_sum = min(min_sum,sum)
        return
     
    # n : 행, j : 열 / 하나씩 확인해보기
    for j in range(N) :
        if visited[j] == 0 :
            visited[j] = 1
            dfs(n + 1, sum + matrix[n][j])
            visited[j] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 10 * N
    
    dfs(0, 0)
    
    print(f'#{tc} {min_sum}')




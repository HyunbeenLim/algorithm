import sys
sys.stdin = open('./sample_input.txt', 'r')

def dfs(r, c, sum_v):
    global min_sum
    
    # 현재 합이 이전까지의 최소합보다 작다면 끝내기
    if sum_v > min_sum:
        return
    
    # 아무 일도 없이 끝까지 도달한다면 최소합 업데이트
    if r == N - 1 and c == N - 1:
        min_sum = min(min_sum, sum_v)
        return
    
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if (nr < N) and (nc < N):
            dfs(nr, nc, sum_v + matrix[nr][nc])
    
T = int(input())

dr = [1, 0]
dc = [0, 1]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    min_sum = 10 * (N ** 2)
    
    dfs(0, 0, matrix[0][0])
    
    print(f'#{tc} {min_sum}')
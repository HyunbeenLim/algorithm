import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

min_cost = sum(map(sum, W))                             # 최소값
visited = [0] * N

def dfs(start, current, cost, cnt):                     # 시작 위치, 현재 위치, 현재까지의 비용과 방문 도시 개수
    global min_cost

    if cost > min_cost:                                 # 가치치기
        return

    if cnt == N - 1:                                    # 모든 도시를 방문했다면
        if W[current][start]:
            cost += W[current][start]
            min_cost = min(min_cost, cost)
        return
    
    for j in range(N):
        if not visited[j] and W[current][j]:            # 방문, 길 여부 확인
            visited[j] = 1
            dfs(start, j, cost+W[current][j], cnt+1)    
            visited[j] = 0

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 0)
    visited[i] = 0

print(min_cost)
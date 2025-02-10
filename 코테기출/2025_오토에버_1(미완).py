import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

# 인접 리스트
graph = [[0] for _ in range(N + 1)]

for _ in range(M):              
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (N + 1)
cnt = 0

for i in range(1, N + 1):
    if not visited[i]:              
        cnt += 1
        visited[i] = 1
        for child in graph[i]:
            visited[child] = 1
        
print(cnt)
    
# 틀림
# 게리멘더링처럼 그룹 별 bfs 돌기
# 각 그룹 별 최대 선택 가능한 정점 구해서 더해주기

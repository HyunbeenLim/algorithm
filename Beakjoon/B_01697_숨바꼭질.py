import sys
input = sys.stdin.readline

from collections import deque

# 방문 리스트 만들기 위해 최대 인덱스 저장
max_idx = 100000
N, K = map(int, input().split())
visited = [0] * (max_idx + 1)

# 일반적인 bfs
def bfs():
    global visited
    q = deque()
    visited[N] = 1
    q.append(N)
    
    while q:
        x = q.popleft()
        if x == K:
            return visited[x] - 1
        
        # 방문하지 않았던 곳만 방문하면 최단거리 구할 수 있음!
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= max_idx and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)


print(bfs())

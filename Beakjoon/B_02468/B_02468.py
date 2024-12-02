import sys
input = sys.stdin.readline

from collections import deque


def bfs(start, rainfall):
    global visited
    r, c = start
    
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] != 1 and heights[nr][nc] > rainfall:
                q.append((nr, nc))
                visited[nr][nc] = 1

# 우 하 좌 상
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

N = int(input())

heights = [list(map(int, input().split())) for _ in range(N)]

max_height = max(map(max, heights))

max_survived = 0
for rain in range(max_height):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if heights[r][c] > rain and not visited[r][c]:
                param = (r, c)
                bfs(param, rain)
                cnt += 1

    if max_survived < cnt:
        max_survived = cnt

print(max_survived)
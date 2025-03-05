import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M = map(int, input().split())
forest = [list(input()) for _ in range(N)]

water = []

# 좌표 찾기
for r in range(N):
    for c in range(M):
        if forest[r][c] == 'S':
            start_r, start_c = r, c
        if forest[r][c] == 'D':
            end_r, end_c = r, c
        if forest[r][c] == '*':
            water.append((r, c))

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 물이 도달하는 시간
def water_bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)]
    for r, c in water:
        q.append((r, c))
        visited[r][c] = 1
    
    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < M) and forest[nr][nc] != 'D' and forest[nr][nc] != 'X' and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

    return visited

water_visited = water_bfs()

# 고슴도치 이동
def bfs():
    q = deque()
    q.append((start_r, start_c))
    visited = [[0] * M for _ in range(N)]
    visited[start_r][start_c] = 1

    while q:
        r, c = q.popleft()

        if (r, c) == (end_r, end_c):
            return visited[r][c] - 1
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc] and forest[nr][nc] != 'X':
                temp_time = visited[r][c] + 1
                if not water_visited[nr][nc] or temp_time < water_visited[nr][nc]:
                    visited[nr][nc] = temp_time
                    q.append((nr, nc))

    return 'KAKTUS'

ans = bfs()
print(ans)
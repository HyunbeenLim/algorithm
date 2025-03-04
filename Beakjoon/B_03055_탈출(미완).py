import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque

R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]

water = []

# 좌표 찾기
for r in range(R):
    for c in range(C):
        if forest[r][c] == 'S':
            start_r, start_c = r, c
        if forest[r][c] == 'D':
            end_r, end_c = r, c
        if forest[r][c] == '*':
            water.append((r, c))

# 3차원 visited
visited = [[[0,0]] * C for _ in range(R) ]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# bfs
def bfs(r, c, type):
    if type == '*':
        idx = 1
    else:
        idx = 0

    q = deque()
    q.append((r, c))
    visited[r][c][idx] = 1

    while q:
        r, c = q.popleft()

        if idx == 0 and r == end_r and c == end_c:
            return visited[r][c][idx] - 1

        for m in range(4):
            nr = r + dr[m]
            nc = c + dc[m]
            if (0 <= nr < R) and (0 <= nc < C) and forest[nr][nc] == '.':
                if not visited[nr][nc][idx]:
                    visited[nr][nc][idx] = visited[r][c][idx] + 1
                    q.append((nr, nc))

    return

# 각 좌표에 물이 도달하는 가장 빠른 시간 저장
for w in water:
    bfs(w[0], w[1], '*')

for frac in forest:
    print(frac)
for frac in visited:
    print(frac)
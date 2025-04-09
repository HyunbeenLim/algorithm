import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

i = 1
while True:
    N = int(input())
    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = cave[0][0]
    q = deque()
    q.append((0, 0))

    while q:
        r, c = q.popleft()
        
        for m in range(4):
            nr = r + dr[m]
            nc = c + dc[m]
            if (0 <= nr < N) and (0 <= nc < N):
                temp = visited[r][c] + cave[nr][nc]

                if temp < visited[nr][nc]:
                    visited[nr][nc] = temp
                    q.append((nr, nc))

    print(f'Problem {i}: {visited[N-1][N-1]}')
    i += 1
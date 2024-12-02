import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_01226_미로1/input.txt', 'r')

from collections import deque

def bfs(start, end):
    global q
    visited = [[0] * N for _ in range(N)]

    # 우 하 좌 상
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # 시작 점 방문 확인
    q.append(start)
    visited[start[0]][start[1]] = 1

    while q:
        row_col = q.popleft()
        r = row_col[0]
        c = row_col[1]

        # 우 하 좌 상 인접점의 이동 여부 확인
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0 and maze[nr][nc] != 1:
                # 목적지 발견하면 1
                if nr == end[0] and nc == end[1]:
                    return 1
                else:
                    # 이동 가능하면 enqueue
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    return 0

for j in range(1, 11):
    N = 16
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = i, j
            elif maze[i][j] == 3:
                end = i, j

    ans = bfs(start, end)

    print(f'#{tc} {ans}')








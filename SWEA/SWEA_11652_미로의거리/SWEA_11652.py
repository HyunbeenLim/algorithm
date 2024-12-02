import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11652_미로의거리/sample_input.txt', 'r')

from collections import deque

def bfs(start):
    global q
    visited = [[0] * N for _ in range(N)]

    # 우 하 좌 상
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # 경로를 보자
    q.append(start)
    visited[start[0]][start[1]] = 1

    while q:
        row_col = q.popleft()
        r = row_col[0]
        c = row_col[1]
        # 찾았으면 숫자 내보내기
        # 이동 거리는 움직인 횟수 - 1
        if maze[r][c] == 3:
            return visited[r][c] - 1
        # 우 하 좌 상 인접점의 이동 여부 확인
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0 and maze[nr][nc] != 1:
                # 이동 가능하면 enqueue
                q.append((nr, nc))
                # 이전 정점보다 +1이 되어야 하지만, 시작 정점과 그 인접점은 모두 1이여야 한다
                if r == start[0] and c == start[1]:
                    visited[nr][nc] = 1
                else:
                    visited[nr][nc] = visited[r][c] + 1
    return 0




T = int(input())

for tc in range(1, T + 1):
    q = deque()
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = i, j

    ans  = bfs(start)

    print(f'#{tc} {ans}')
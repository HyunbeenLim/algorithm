from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def bfs():
        q = deque()
        visited = [[0] * M for _ in range(N)]

        q.append((0, 0))
        visited[0][0] = 1

        while q:
            r, c = q.popleft()

            if (r, c) == (N-1, M-1):
                return visited[r][c]

            for m in range(4):
                nr = r + dr[m]
                nc = c + dc[m]
                if (0 <= nr < N) and (0 <= nc < M) and maps[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

        return -1

    return bfs()

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
from collections import deque

def solution(land):
    N = len(land)
    M = len(land[0])

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited = [[0] * M for _ in range(N)]
    oil_by_column = [0] * M

    # 석유 블럭 단위 bfs
    for start_r in range(N):
        for start_c in range(M):
            if land[start_r][start_c] == 0 or visited[start_r][start_c] == 1:
                continue

            q = deque()
            q.append((start_r, start_c))
            visited[start_r][start_c] = 1

            oil_count = 0
            # 지금 순회하고 있는 석유 덩어리가 지나는 모든 열 기록
            columns = set()

            while q:
                r, c = q.popleft()

                oil_count += 1
                columns.add(c)
                
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc] and land[nr][nc] == 1:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
            
            # 방금 순회한 석유 덩어리가 지나는 모든 열에 해당 덩어리의 크기를 더해줌
            for c in columns:
                oil_by_column[c] += oil_count

    return max(oil_by_column)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
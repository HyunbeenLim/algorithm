from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])

    for r in range(N):
        for c in range(M):
            if maps[r][c] == "S":
                start_r, start_c = r, c
    
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    q = deque()
    q.append((start_r, start_c))

    # 레버 찾기 이전
    visited = [[0] * M for _ in range(N)]
    visited[start_r][start_c] = 1

    # 레버 찾은 이후
    after_lever = [[0] * M for _ in range(N)]
    found_lever = False

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 레버 찾기 전엔 레버를 찾는 것을 최우선으로 한다
            if (0 <= nr < N) and (0 <= nc < M) and maps[nr][nc] != "X" and not found_lever:
                if not visited[nr][nc]:
                    # 레버 찾은 이후엔 레버 위치부터 다시 bfs를 돌 수 있도록 해야 한다
                    if maps[nr][nc] == "L":
                        found_lever = True
                        q.clear()
                        after_lever[nr][nc] = visited[r][c]
                        q.append((nr, nc))
                        break
                    else:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1
            # 레버 찾은 이후 출구 찾기
            elif (0 <= nr < N) and (0 <= nc < M) and maps[nr][nc] != "X" and found_lever and not after_lever[nr][nc]:
                if maps[nr][nc] == "E":
                    return after_lever[r][c] + 1
                else:
                    q.append((nr, nc))
                    after_lever[nr][nc] = after_lever[r][c] + 1
    # 레버를 찾지 못했거나, 출구를 찾지 못했을 경우 -1
    else:
        return -1


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
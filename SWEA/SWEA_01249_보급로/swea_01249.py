import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

################ bfs ################
# 최단 경로를 찾는 것이 아닌, 최소 비용을 찾는 문제
# bfs는 목표 좌표를 찾자마자 return 해줘서 최단 경로를 찾지만
# 얘는 그렇게 하면 최소 비용을 찾지 못함
# 목표 좌표를 찾아도 함수가 끝까지 돌아가게 해야 최소 비용을 찾을 수 있음

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    q = deque()
    q.append((0, 0))

    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = field[0][0]

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0 <= nr < N) and (0 <= nc < N):
                temp = visited[r][c] + field[nr][nc]
                if temp < visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = temp

    return  visited[N-1][N-1]

for tc in range(1, int(input()) + 1):
    N = int(input())

    field = [list(map(int, input())) for _ in range(N)]

    ans = bfs()

    print(f'#{tc} {ans}')



################ 다익스트라 ################

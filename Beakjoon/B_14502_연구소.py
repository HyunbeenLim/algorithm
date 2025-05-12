import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from itertools import combinations
from collections import deque
import copy

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸
empty = []

# 바이러스가 있는 칸
virus = []
non_safe = 0

for r in range(N):
    for c in range(M):
        if lab[r][c] == 0:
            empty.append((r, c))
        if lab[r][c] == 2:
            virus.append((r, c))
            non_safe += 1
        if lab[r][c] == 1:
            non_safe += 1

non_safe += 3

# 벽을 설치할 좌표
wall_combi = list(combinations(empty, 3))

max_safe = 0
min_virus = N * M + 1

# bfs 함수 정의
def bfs(coord):
    global max_safe, min_virus

    q = deque(virus)
    current_virus_cnt = non_safe
    copy_lab = copy.deepcopy(lab)

    for r, c in coord:
        copy_lab[r][c] = 1

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < M) and copy_lab[nr][nc] == 0:
                copy_lab[nr][nc] = 2
                q.append((nr, nc))
                current_virus_cnt += 1

                # 지금까지 최소 바이러스 수보다 현재 함수의 바이러스 수가 크면 종료
                if current_virus_cnt > min_virus:
                    return
    
    current_safe = N * M - current_virus_cnt
    if current_safe > max_safe:
        max_safe = current_safe
        min_virus = current_virus_cnt
    
    return

for coord in wall_combi:
    bfs(coord)

print(max_safe)
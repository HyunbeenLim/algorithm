import sys
input = sys.stdin.readline

from collections import deque

cctv = [1, 2, 3, 4, 5]

# 우 하 좌 상
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# cctv 별 방향
order = [
    0, 
    [(0,), (1,), (2,), (3,)],       # 순회 가능하게 튜플로 넣어줌 
    [(0, 2), (1, 3)], 
    [(0, 3), (2, 3), (1, 2), (0, 1)], 
    [(0, 2, 3), (1, 2, 3), (0, 1, 3), (0, 1, 2)], 
    [(0, 1, 2, 3)]
    ]

N, M = map(int, input().split())
move = max(N, M)

office = [list(map(int, input().split())) for _ in range(N)]

cctv_list = deque()

dead_spot = 0
for r in range(N):
    for c in range(M):
        if office[r][c] == 0:
            dead_spot += 1                          # 사각지대
        elif office[r][c] in cctv:
            cctv_list.append((office[r][c], r, c))  # cctv 번호와 좌표

def possibility_cnt(direction, r, c):
    cnt = 0

    for m in range(1, move + 1):
        nr = r + dr[direction] * m
        nc = c + dc[direction] * m
        if (0 <= nr < N) and (0 <= nc < M) and (office[nr][nc] != '#') and (office[nr][nc] not in cctv):
            if office[nr][nc] != 6:
                cnt += 1
            else:
                return cnt
    return cnt

def office_manipulate(direction, r, c):
    global office

    for m in range(1, move + 1):
        nr = r + dr[direction] * m
        nc = c + dc[direction] * m
        if (0 <= nr < N) and (0 <= nc < M) and (office[nr][nc] != '#') and (office[nr][nc] not in cctv):
            if office[nr][nc] != 6:
                office[nr][nc] = '#'
            else:
                return


def monitor():
    global dead_spot

    number, r, c = cctv_list.popleft()
    ways = order[number]

    temp_list = []

    # 최대로 보는 방향 찾기
    for way in ways:
        temp_cnt = 0
        for direction in way:
            cnt = possibility_cnt(direction, r, c)
            temp_cnt += cnt

        temp_list.append(temp_cnt + 1)

    max_watch = max(temp_list)

    # 최대 구간
    best = order[number][temp_list.index(max_watch)]

    for direction in best:
        office_manipulate(direction, r, c)

    dead_spot -= max_watch

while cctv_list:
    monitor()

print(dead_spot)
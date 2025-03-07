import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M = 12, 6

field = [list(input()) for _ in range(N)]

# 터트릴 수 있는지 확인하는 함수
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(start_r, start_c, color):
    global checked
    q = deque()
    q.append((start_r, start_c))
    visited = [[0] * M for _ in range(N)]
    visited[start_r][start_c] = 1
    color_cnt = 1
    temp_boom = []

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc] and field[nr][nc] == color:
                checked.append((nr, nc))
                temp_boom.append((nr, nc))
                q.append((nr, nc))
                visited[nr][nc] = 1
                color_cnt += 1

    if color_cnt >= 4:
        temp_boom.append((start_r, start_c))
        return temp_boom
    else:
        return False

# 내리는 함수
def reconstruct():
    global field

    for r in range(N-1):
        for c in range(M):
            current = r
            while current >= 0 and field[current][c] != '.' and field[current+1][c] == '.':
                field[current][c], field[current+1][c] = field[current+1][c], field[current][c]
                current -= 1
    return


cnt = 0

while True:
    # 확인한 좌표
    checked = []

    # 터트릴 좌표
    boom = []

    # 순회
    for r in range(N):
        for c in range(M):
            if field[r][c] != '.' and (r, c) not in checked:
                find = bfs(r, c, field[r][c])
                if find:
                    boom.append(find)
    
    if boom:
        cnt += 1
        for frac in boom:
            for r, c in frac:
                field[r][c] = '.'
        reconstruct()
    else:
        break

print(cnt)
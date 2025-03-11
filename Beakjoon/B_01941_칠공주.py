import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque

N = 5
seats = [list(input().strip()) for _ in range(N)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 7개의 좌표가 연결되어 있는지 확인하는 함수
## 좌표 7개가 담긴 리스트를 넣어주기
def bfs(cells):
    q = deque()
    r, c = cells[0]
    q.append((r, c))

    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1

    # 연결된 셀의 개수
    checked_cell = 1

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 연결된 셀인지 확인
            if (0 <= nr < N) and (0 <= nc < N) and not visited[nr][nc] and (nr, nc) in cells:
                visited[nr][nc] = 1
                q.append((nr, nc))
                checked_cell += 1

    return True if checked_cell == 7 else False

# 25개의 좌표에서 7개를 뽑는 경우의 수 구하기(0 ~ 24번 중 번호 7개 선택하는 방식)

# 좌표
rc_lst = []
for i in range(N ** 2):
    rc_lst.append((i // 5, i % 5))

# 좌표 담을 리스트
cells = [0] * 7
ans = 0
q = deque()

def dfs(depth, start, S_cnt, Y_cnt):
    global ans

    if Y_cnt >= 4:
        return

    if depth == 7:
        if bfs(cells):
            ans += 1
        return

    for i in range(start, N ** 2):  # 이전 좌표보다 앞 좌표만 선택하게 해 중복 피하기
        cells[depth] = rc_lst[i]
        if seats[rc_lst[i][0]][rc_lst[i][1]] == 'S':
            dfs(depth+1, i+1, S_cnt+1, Y_cnt)
        else:
            dfs(depth+1, i+1, S_cnt, Y_cnt+1)

dfs(0, 0, 0, 0)
print(ans)
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque

M, N, H = map(int, input().split())

storage = [[[0] * H for _ in range(M)] for _ in range(N)]
visited = [[[0] * H for _ in range(M)] for _ in range(N)]
unripe = 0
q = deque()

# 1 익은 토마토, 0 안 익은 토마토, -1 빈칸
for f in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(M):
            storage[r][c][f] = box[r][c]
            if box[r][c] == 1:
                q.append((r, c, f))
                visited[r][c][f] = 1
            if box[r][c] == 0:
                unripe += 1

# 층
df = [-1, 1]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

days = -1
while q:
    days += 1

    # 날짜를 세려면 이렇게 해야 함!
    for _ in range(len(q)):
        r, c, f = q.popleft()

        # 같은 층 탐색
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc][f] and not storage[nr][nc][f]:
                unripe -= 1
                visited[nr][nc][f] = 1
                storage[nr][nc][f] = 1
                q.append((nr, nc, f))
                
        # 위 아래 층 탐색
        for k in range(2):
            nf = f + df[k]
            if (0 <= nf < H) and not visited[r][c][nf] and not storage[r][c][nf]:
                unripe -= 1
                visited[r][c][nf] = 1
                storage[r][c][nf] = 1
                q.append((r, c, nf))

if unripe:
    print(-1)
else:
    print(days)

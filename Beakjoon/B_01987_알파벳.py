import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

## 백트래킹

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

max_cnt = 0
visited = [[0] * M for _ in range(N)]
alphabet = set()

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, cnt):
    global max_cnt

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc] and board[nr][nc] not in alphabet:
            # 방문 체크
            visited[nr][nc] = 1
            alphabet.add(board[nr][nc])
            dfs(nr, nc, cnt+1)
            # 백트래킹
            visited[nr][nc] = 0
            alphabet.remove(board[nr][nc])
    # 아무 곳도 갈 수 없는 경우
    else:
        max_cnt = max(max_cnt, cnt)
        return

# 시작점 방문 체크 후 시작
visited[0][0] = 1
alphabet.add(board[0][0])
dfs(0, 0, 1)
print(max_cnt)
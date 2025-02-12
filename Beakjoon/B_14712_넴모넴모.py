import sys
input = sys.stdin.readline

def dfs(r, c):          # 현재 좌표, 순회한 칸 수
    global board, cnt

    if r == N:
        cnt += 1
        return
    
    nr, nc = (r, c + 1) if (c + 1) < M else (r + 1, 0)

    # 두지 않을 때
    dfs(nr, nc)

    # 둘 때
    if r > 0 and c > 0 and board[r-1][c] and board[r][c-1] and board[r-1][c-1]:
        return
    board[r][c] = 1
    dfs(nr, nc)
    ## 복구
    board[r][c] = 0
    
N, M = map(int, input().split())
board =  [[0] * M for _ in range(N)]        # 게임판

cnt = 0

dfs(0, 0)

print(cnt)

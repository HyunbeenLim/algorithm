import sys
input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]
cnt = 0

# 열 방문 표시
visited = [0] * N

def check_diagonal(start_r, start_c):
    # 왼쪽 위
    left_r, left_c = start_r - 1, start_c - 1
    while left_r >= 0 and left_c >= 0:
        if board[left_r][left_c] == 1:
            return False
        left_r -= 1
        left_c -= 1

    # 오른쪽 위
    right_r, right_c = start_r - 1, start_c + 1
    while right_r >= 0 and right_c < N:
        if board[right_r][right_c] == 1:
            return False
        right_r -= 1
        right_c += 1
    
    return True

def dfs(depth):     # 깊이(행), 현재까지 배치한 퀸
    global board, cnt, visited

    # 모든 퀸을 배치했다면 cnt 올려주고 종료
    if depth == N:
        cnt += 1
        return
    
    for c in range(N):
        # 방문하지 않았고, 위 대각선에 퀸이 없다면
        if not visited[c] and check_diagonal(depth, c):
            visited[c] = 1
            board[depth][c] = 1
            dfs(depth+1)
            visited[c] = 0
            board[depth][c] = 0

dfs(0)

print(cnt)
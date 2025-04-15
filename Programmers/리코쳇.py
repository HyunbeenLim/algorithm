from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 위치 찾는 함수
def find_position(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'R':
                start = (r, c)
            if board[r][c] == 'G':
                # 목표 지점에 도달 가능한지 확인
                for m in range(4):
                    nr = r + dr[m]
                    nc = c + dc[m]
                    # G가 벽과 맞닿아 있거나 board[nr][nc]가 장애물일때
                    if not (0 <= nr < len(board)) or not (0 <= nc < len(board[0])) or board[nr][nc] == 'D':
                        goal = (r, c)
                        break
                # 불가능 하다면
                else:
                    return False
    return {
        'start': start,
        'goal': goal
    }

# 이동 함수
def move(r, c, direction, board):
    while True:
        nr, nc = r + dr[direction], c + dc[direction]

        if not (0 <= nr < len(board)) or not (0 <= nc < len(board[0])) or board[nr][nc] == 'D':
            return (r, c)
        r, c = nr, nc

def solution(board):
    find = find_position(board)
    # 목표 지점에 도달할 수 없을 때 바로 -1 -> 이건 굳이 안 해도 되는데 그냥 했음
    if not find:
        return -1
    else:
        start_r, start_c = find['start']
        goal_r, goal_c = find['goal']

        visited = [[0] * (len(board[0])) for _ in range(len(board))]
        q = deque()
        q.append((start_r, start_c))
        visited[start_r][start_c] = 1

        while q:
            r, c = q.popleft()

            if (r, c) == (goal_r, goal_c):
                return visited[r][c] - 1
            
            for m in range(4):
                nr, nc = move(r, c, m, board)
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
        return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
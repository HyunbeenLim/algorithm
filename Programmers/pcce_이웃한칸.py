def solution(board, h, w):
    N = len(board)
    M = len(board[0])

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    target = board[h][w]
    ans = 0

    for k in range(4):
        nr = h + dr[k]
        nc = w + dc[k]
        if (0 <= nr < N) and (0 <= nc < M) and board[nr][nc] == target:
            ans += 1

    return ans


print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1))
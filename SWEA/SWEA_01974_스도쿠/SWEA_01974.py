# 3 x 3 행렬 확인
def triple(sr, sc, er, ec):
    visited = [0] * 10
    for r in range(sr, er + 1):
        for c in range(sc, ec + 1):
            if visited[matrix[r][c]] == 0:
                visited[matrix[r][c]] = 1
            # 방문했던 적이 있다면 바로 False
            else:
                return False
    # 아무 일 없었다면 True
    return True

# 행, 열 확인
def row_col_check():
    for i in range(N):
        row_visited = [0] * 10
        col_visited = [0] * 10
        for j in range(N):
            if row_visited[matrix[i][j]] == 0 and col_visited[matrix[j][i]] == 0:
                row_visited[matrix[i][j]] = 1
                col_visited[matrix[j][i]] = 1
            # 방문했던 적이 있다면 바로 False
            else:
                return False
    # 아무 일 없다면 True
    return True

# 최종 함수
def total_check():
    for r in range(1, 4):
        sr = (r - 1) * 3
        er = r * 3 - 1
        for c in range(1, 4):
            sc = (c - 1) * 3
            ec = c * 3 - 1
            if not triple(sr, sc, er, ec):
                return 0
    if row_col_check():
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, T + 1):
    N = 9
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    ans = total_check()
    print(f'#{tc} {ans}')
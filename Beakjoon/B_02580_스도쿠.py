import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

'''
스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.
'''

board = [list(map(int, input().split())) for _ in range(9)]

# 0 좌표 저장
zero_lst = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            zero_lst.append((r, c))

# 행, 열 체크 함수
def row_col_check(r, c, num):
    for i in range(9):
        if num in (board[r][i], board[i][c]):
            return False
    return True

# 3x3 블럭 체크 함수
def block_check(r, c, num):
    # 구간 정하기
    ## 시작 좌표
    sr, sc = (r//3)*3, (c//3)*3
    ## 끝 좌표
    er, ec = sr + 2, sc + 2

    for i in range(sr, er+1):
        for j in range(sc, ec+1):
            if board[i][j] == num:
                return False
    return True

# 백트래킹
def dfs(depth):
    global board

    if depth == len(zero_lst):
        for row in board:
            print(*row)
        # 정답을 찾은 경우 True 반환 => 아래 for 문 안 조건에서 True를 만나면 함수를 종료할 수 있게
        return True
    
    for i in range(1, 10):
        r, c = zero_lst[depth][0], zero_lst[depth][1]
        # 해당 숫자를 넣을 수 있는지 확인
        if row_col_check(r, c, i) and block_check(r, c, i):
            # 넣을 수 있다면 다음으로 진행
            board[r][c] = i
            # 다음 단계에서 True가 반환되면 재귀 호출 완전 종료
            if dfs(depth+1):
                return
            board[r][c] = 0


dfs(0)
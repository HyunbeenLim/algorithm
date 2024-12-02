import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11315_오목/sample_input.txt', 'r')

def check(matrix, N):
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 'o':
                for k in range(4):
                    for m in range(1, 5):
                        dr = r + m * r_delta[k]
                        dc = c + m * c_delta[k]
                        if (0 <= dr < N) and (0 <= dc < N):
                            if matrix[dr][dc] != 'o':
                                break
                        # 인덱스가 넘어갔을 때 확실히 멈춰줘야 제대로 동작함
                        else: break
                    else:
                        return 'YES'
    return 'NO'

T = int(input())

r_delta = [0, 1, 1, 1]
c_delta = [1, 0, 1, -1]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = check(board, N)
    
    print(f'#{tc} {ans}')
    

    
# 두번째 풀기

T = int(input())

dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

def check():
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                for k in range(4):
                    for m in range(1, 5): # 4칸 체크
                        nr = r + m * dr[k]
                        nc = c + m * dc[k]
                        if (0 <= nr < N) and (0 <= nc < N):
                            if board[nr][nc] != 'o':
                                break
                        else: break
                    else: return 'YES'
    return 'NO'

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    
    ans = check()
    print(f'#{tc} {ans}')
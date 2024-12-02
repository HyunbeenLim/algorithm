import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01979_어디에단어가/input.txt', 'r')

T = int(input())

# 행 탐색
def row_search(matrix, K):        
    cnt = 0
    for r in range(N):
        one_cnt = 0
        for c in range(N):
            if matrix[r][c] == 1:
                one_cnt += 1
            else:
                if one_cnt == K:
                    cnt += 1
                    one_cnt = 0
                else:
                    one_cnt = 0
        if one_cnt == K:
            cnt += 1
    return cnt

# 열 탐색
def col_search(matrix, K):        
    cnt = 0
    for c in range(N):
        one_cnt = 0
        for r in range(N):
            if matrix[r][c] == 1:
                one_cnt += 1
            else:
                if one_cnt == K:
                    cnt += 1
                    one_cnt = 0
                else:
                    one_cnt = 0
        if one_cnt == K:
            cnt += 1
    return cnt

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = row_search(puzzle, K) + col_search(puzzle, K)
    
    print(f'#{tc} {ans}')


            
                
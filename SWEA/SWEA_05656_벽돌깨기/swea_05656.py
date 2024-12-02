import sys
sys.stdin = open('sample_input.txt', 'r')

##################### 내꺼 #####################
from itertools import product
import copy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 벽돌 깨는 함수(재귀)
def smash(r, c, value):    # 깨질 벽돌 좌표, 벽돌 번호
    global mat, copy_cnt

    if mat[r][c] == 0:
        return
    mat[r][c] = 0
    
    # 깨진 벽돌 count
    copy_cnt -= 1
    if value == 1:
        return
    else:
        for d in range(4):
            for m in range(1, value):
                nr = r + m * dr[d]
                nc = c + m * dc[d]
                if (0 <= nr < H) and (0 <= nc < W):
                    smash(nr, nc, mat[nr][nc])

# 새로 생긴 빈공간으로 블럭 내리기
def reconstruct():
    global mat
    
    for r in range(H - 1):
        for c in range(W):
            cur = r
            while cur >= 0 and mat[cur][c] != 0 and mat[cur + 1][c] == 0:
                mat[cur][c], mat[cur + 1][c] = mat[cur + 1][c], mat[cur][c]
                cur -= 1
    
for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())

    # 원본
    field = [list(map(int, input().split())) for _ in range(H)]
    # 블럭 수
    block_cnt = 0

    for r in range(H):
        for c in range(W):
            if field[r][c] != 0:
                block_cnt += 1

    # 구슬 떨어트리는 순서 조합(cartesian product)
    order = product(list(range(W)), repeat=N)
    
    min_cnt = W * H

    for comb in order:
        mat = copy.deepcopy(field)
        copy_cnt = block_cnt
        for col in comb:
            for row in range(H):
                if mat[row][col] != 0:
                    break
            smash(row, col, mat[row][col])
            reconstruct()
        min_cnt = min(min_cnt, copy_cnt)
        if min_cnt == 0:
            break
    
    print(f'#{tc} {min_cnt}')
        



##################### 강사님 #####################
# 방향설정 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def back_track(level, remains, cur_arr):
    global min_blocks
 
    # 종료 조건
    if level == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return
 
    for c in range(W):
        # 현재 배열 복사해서 터트리기
        copy_arr = [row[:] for row in cur_arr]
 
        row = -1
        for r in range(H):
            if copy_arr[r][c] != 0:
                row = r
                break
        if row == -1:
            continue
 
        lst = [(row, c, copy_arr[row][c])]  # 앞으로 깨질 벽돌 저장
        cur_remains = remains -1            # 현재 남은벽돌 -1
        copy_arr[row][c] = 0                # 현재 벽돌 깨기
 
        while lst:
            r, c, p = lst.pop()
            for k in range(1,p):
                for i in range(4):
                    nr = r + (dr[i] * k)
                    nc = c + (dc[i] * k)
 
                    if 0 <= nr < H and 0 <= nc < W and copy_arr[nr][nc] != 0:
                        lst.append((nr,nc,copy_arr[nr][nc]))
                        copy_arr[nr][nc] =0
                        cur_remains -= 1
 
        # 빈간 메꾸기
        for c in range(W):
            idx = H -1
            for r in range(H-1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1
        back_track(level+1, cur_remains, copy_arr)
 
T = int(input())
for test_case in range(1,T+1):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
 
    min_blocks = float('inf')
    blocks = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1
 
    back_track(0, blocks, arr)
    print(f'#{test_case} {min_blocks}')





    
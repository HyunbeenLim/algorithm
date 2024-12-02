import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_01211/input.txt", "r")
# input = sys.stdin.readline


def moving_count(matrix, col_idx):
    x = 0
    y = col_idx

    cnt = 0
    while True:
        # 일단 한칸 내려가기
        x += 1
        cnt += 1

        if y-1 >= 0 and matrix[x][y - 1]:
            # 왼쪽 쭉 가보기
            search_0 = matrix[x]
            for ny in range(y-1, -1, -1): # ny: y-1 ~ 0
                if search_0[ny] == 0:
                    cnt += (y - ny - 1)
                    y = ny + 1
                    break
            # 벽면 부딪히면 ny가 해당 위치에서 멈춤 -> ny로 업데이트
            else:
                y = ny
        elif y+1 < N and matrix[x][y + 1]:
            # 오른쪽 쭉 가보기
            search_0 = matrix[x]
            for ny in range(y + 1, N):
                if search_0[ny] == 0:
                    cnt += (ny - 1 - y)
                    y = ny - 1
                    break
            # 벽면 부딪히면 ny가 해당 위치에서 멈춤 -> ny로 업데이트
            else:
                y = ny

        if x == 99:
            break

    return col_idx, cnt



for t in range(10):
    tc = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]

    start_idices = []
    search_1 = matrix[0]

    for i in range(N):
        if search_1[i] == 1:
            start_idices.append(i)
    
    min_cnt = float('inf')
    min_idx = 0
    # 여기서 뭔가 잘못 됨
    for idx in start_idices:
        result_idx, result_cnt = moving_count(matrix, idx)
        if min_cnt >= result_cnt:
            min_cnt = result_cnt
            min_idx = result_idx
    
    print(f'{tc} {min_idx}')

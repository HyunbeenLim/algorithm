import sys
sys.stdin = open('./sample_input.txt', 'r')

# def check(sr, sc, length):
#     for r in range(sr, sr + length):
#         for c in range(sc, sc + length):
#             if matrix[r][c] != '#':
#                 return 'no'
#     else:
#         return 'yes'
    

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     matrix = [list(input()) for _ in range(N)]

#     for r in range(N):
#         length = 0
#         for c in range(N):
#             # 칼럼 끝나는 부분 잘 선택하면 된다
#             if matrix[r][c] == '#':
#                 sr, ec = r, c
#                 length += 1
#         if length > 0:
#             break
    
#     ans = check(sr, ec - length + 1, length)

#     print(f'#{tc} {ans}')





# #을 찾는 함수
def where_start(arr):
    global is_true
    # 모든 행에 대해서
    for r in range(N):
        # 모든 열에 대해서
        for c in range(N):
            # '#'을 발견하면 r,c 저장
            if arr[r][c] == '#':
                length = 0
                i = 0
                # 행열을 돌면서 #이 가로로 연속되는 것만 일단 찾아서 변의 길이(length) 기록
                while (0<= r+i< N)  and arr[r+i][c] == '#':
                    length += 1
                    i += 1
                return r,c, length


# 변의 길이를 기록했으면, 시작점 r,c부터 (r+length)(c+length)까지 전부 '#' 이어야함
def inner_sqr(r, c, length, arr):
    global is_true, shop

    for n in range(length):
        for k in range(length):
            if 0<= r+n < N and 0 <= c+k < N:
                if arr[r + n][c + k] != '#':
                    is_true = 'no'
                    return
                else:
                    shop += 1
            # 범위를 벗어난다면
            else:
                is_true = 'no'
                return
    return


T = int(input())

for tc in range(1, T+1):
    # . : 비어있다. # : 막혀있다.
    N = int(input())
    arr = [input() for _ in range(N)]

    is_true = 'yes'
    # 전체 circle 에 있는 # 개수
    cnt = 0
    for q in range(N):
        for p in range(N):
            if arr[q][p] == '#':
                cnt += 1

    # innercircle에 있는 # 개수
    shop = 0
    r, c, length = where_start(arr)
    inner_sqr(r, c, length, arr)
    if cnt != shop:
        is_true = 'no'
    print(f'#{tc} {is_true}')


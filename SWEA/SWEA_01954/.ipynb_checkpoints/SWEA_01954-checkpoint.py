import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_01954/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    matrix = [[0] * n for _ in range(n)]
    
    r = 0 
    c = -1
    direction = 0

    dr = [1, -1] # 행 방향 조정
    dc = [1, -1] # 열 방향 조정

    num = 1

    while num <= (n ** 2):
        # 방향에 따라 행, 열 방향 조정
        if direction == 0:
            c += dc[0]
        elif direction == 1:
            r += dr[0]
        elif direction == 2:
            c += dc[1]
        elif direction == 3:
            r += dr[1]

        # 전환 조건 고려 후, 방향 업데이트
        if (0 <= r < n) and  (0 <= c < n) and (not matrix[r][c]):
            matrix[r][c] = num
            num += 1
        else:
            if direction == 0:
                c -= dc[0]
            elif direction == 1:
                r -= dr[0]
            elif direction == 2:
                c -= dc[1]
            elif direction == 3:
                r -= dr[1]
            direction = (direction + 1) % 4
    
    print(f'#{tc}')
    for row in matrix:
        print(*row)


# 조금 더 깔끔하게 

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    
    # 방향 지시, 전환
    direction = 0
    delta = [1, 1, -1, -1]
    
    x = 0
    y = -1
    num = 1
    
    while num <= (N ** 2):
        # 방향 지시
        move = delta[direction] 
        ## direction이 1,3 이면 행, 0,2면 열에 연산
        if direction % 2:
            x += move
        else:
            y += move
        
        # 인덱스 확인 후 num 넣기
        ## matrix[x][y]가 True면 숫자를 넣을 수 없음
        if (0 <= x < N) and (0 <= y < N) and (not matrix[x][y]):
            matrix[x][y] = num
            num += 1 # num 업데이트
        # 조건에 하나라도 걸렸을 때, 다시 돌아가기 + 방향 업데이트
        else:
            if direction % 2:
                x -= move
            else:
                y -= move
            direction = (direction + 1) % 4
    
    print(f'#{tc}')
    for row in matrix:
        print(*row)


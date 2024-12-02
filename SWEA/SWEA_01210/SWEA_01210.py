import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_01210/input.txt", "r")
# input = sys.stdin.readline

for t in range(1, 11):
    tc = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    y = 0
    for i in range(N):
        if matrix[99][i] == 2:
            y = i
            break
    x = 99
    while x:
        # 일단 한칸 올라가기
        x -= 1
        if y-1 >= 0 and matrix[x][y - 1]:
            # 왼쪽 쭉 가보기
            search_0 = matrix[x]
            for ny in range(y-1, -1, -1): # ny: y-1 ~ 0
                if search_0[ny] == 0:
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
                    y = ny - 1
                    break
            # 벽면 부딪히면 ny가 해당 위치에서 멈춤 -> ny로 업데이트
            else:
                y = ny

    print(f'#{tc} {y}')
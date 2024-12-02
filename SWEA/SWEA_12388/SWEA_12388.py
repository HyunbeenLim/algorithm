import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12388/sample_input.txt", "r")
# input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    color_matrix = [list(map(int, input().split())) for _ in range(n)]

    matrix_to_fill = [[0] * 10 for _ in range(10)]

    for c in range(n):
        color_indicator = color_matrix[c]
        # 빨강 1, 파랑 2
        color = color_indicator[4]
        x1, y1, x2, y2 = color_indicator[:4]
        
        # 색칠하기 == 숫자 더하기
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                matrix_to_fill[i][j] += color

    violet_cnt = 0

    for i in range(10):
        for j in range(10):
            if matrix_to_fill[i][j] >= 3:
                violet_cnt += 1
    
    print(f'#{tc} {violet_cnt}')



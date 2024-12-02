import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_11008/sample_input.txt", "r")
# input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    max_sum = 0
    ij_sum = 0

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            ij_sum = matrix[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < n) and (0 <= nj < n):
                    ij_sum += matrix[ni][nj]
            if max_sum < ij_sum:
                max_sum = ij_sum
    print(f'#{tc} {max_sum}')
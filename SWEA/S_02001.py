import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    fly_mat = [[0] * (N + 1)]
    for i in range(N):
        row = [0] + list(map(int, input().split())) # 원래 행렬
        fly_mat.append(row)

    sum_mat = [[0] * (N + 1) for _ in range(N + 1)] # 합 행렬
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            sum_mat[i][j] = sum_mat[i - 1][j] + sum_mat[i][j - 1] + fly_mat[i][j] - sum_mat[i - 1][j - 1]

    max_kill = 0

    for i in range(1, N - M + 1): # 사각형의 왼쪽 맨 위 인덱스의 최대 값이 N - M + 1
        for j in range(1, N - M + 1):
            fly_kill = sum_mat[i + M - 1][j + M - 1] - sum_mat[i - 1][j + M - 1] - sum_mat[i + M - 1][j - 1] + sum_mat[i - 1][j - 1]
            if fly_kill > max_kill:
                max_kill = fly_kill
    
    print(f'#{tc} {max_kill}')
    

# tc 몇 가지 틀린 답 나오는데 왜 틀린지 모르겠음
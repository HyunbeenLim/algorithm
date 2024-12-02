import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12394', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    ans = ''

    # 행 탐색 (왼쪽에서 오른쪽으로)
    for i in range(N):  # i: 0 ~ N-1
        for j in range(N-M+1):  # j: 0 ~ N-M
            # M을 반으로 나눠서 앞 뒤로 같은지 비교
            for d in range(M//2):
                # 앞 인덱스
                nj1 = j + d
                # 뒤 인덱스
                nj2 = j + (M-1) - d
                # 다르면 for 문 탈출, j 한 칸 앞으로 간 뒤 다시 확인
                if matrix[i][nj1] != matrix[i][nj2]:
                    break
            # break하지 않았다 = 회문이다
            else:
                for s in range(j, j + M):
                    ans += matrix[i][s]


    # 열 탐색 (위에서 아래로)
    for j in range(N):
        for i in range(N-M+1):
            for d in range(M//2):
                ni1 = i + d
                ni2 = i + (M-1) - d
                if matrix[ni1][j] != matrix[ni2][j]:
                    break
            else:
                for s in range(i, i + M):
                    ans += matrix[s][j]
    
    print(f'#{tc} {ans}')
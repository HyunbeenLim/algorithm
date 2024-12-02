import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01216_회문2/input.txt', 'r')

for j in range(1, 11):
    tc = int(input())
    N = 100
    matrix = [list(input()) for _ in range(N)]
    length = 0

    # 행 탐색 (왼쪽에서 오른쪽으로)
    for m in range(N):
        for i in range(N):  # i: 0 ~ N-1
            for j in range(N-m+1):  # j: 0 ~ N-M
                # M을 반으로 나눠서 앞 뒤로 같은지 비교
                for d in range(m//2):
                    # 앞 인덱스
                    nj1 = j + d
                    # 뒤 인덱스
                    nj2 = j + (m-1) - d
                    # 다르면 for 문 탈출, j 한 칸 앞으로 간 뒤 다시 확인
                    if matrix[i][nj1] != matrix[i][nj2]:
                        break
                # break하지 않았다 = 회문이다
                else:
                    length = m


    # 열 탐색 (위에서 아래로)
    for m in range(N):
        for j in range(N):
            for i in range(N-m+1):
                for d in range(m//2):
                    ni1 = i + d
                    ni2 = i + (m-1) - d
                    if matrix[ni1][j] != matrix[ni2][j]:
                        break
                else:
                    length = m

    print(f'#{tc} {length}')




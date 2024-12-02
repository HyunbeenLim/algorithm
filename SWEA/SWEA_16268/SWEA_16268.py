import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_16268/input1.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    petal_matrix = [list(map(int, input().split())) for _ in range(n)]

    # 방향: 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 최대 꽃잎 개수
    max_petal = 0
    for i in range(n):
        for j in range(m):
            petal = petal_matrix[i][j]
            for k in range(4):
                di = i + dr[k]
                dj = j + dc[k]
                # 나가면 더하지 말자
                if (0 <= di < n) and (0 <= dj < m):
                    petal += petal_matrix[di][dj]
            if max_petal <= petal:
                max_petal = petal
    
    print(f'#{tc} {max_petal}')

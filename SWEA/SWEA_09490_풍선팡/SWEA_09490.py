import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_09490_풍선팡/input1.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # N - 행, M - 열
    N, M = map(int, input().split())
    petal_matrix = [list(map(int, input().split())) for _ in range(N)]

    # 델타 우 하 좌 상
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    max_petal = 0
    
    for r in range(N):
        for c in range(M):
            # 현재 위치의 꽃잎 개수
            petal_rc = petal_matrix[r][c]
            petal_num = petal_rc
            # 인접 풍선 터트리기
            for m in range(1, petal_num + 1):
                for k in range(4):
                    nr = r + dr[k] * m
                    nc = c + dc[k] * m
                    if (0 <= nr < N) and (0 <= nc < M):
                        petal_rc += petal_matrix[nr][nc]
            if max_petal < petal_rc:
                max_petal = petal_rc

    print(f'#{tc} {max_petal}')
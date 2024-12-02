# 문제 1 미생물 이동

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 델타 방법 - 우 하 좌 상 순서
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # 초기 최댓값 설정
    max_feed = float('-inf')

    for i in range(N):
        for j in range(N):
            current_feed = 0
            # 현재 위치 먹이 더하기
            current_feed += matrix[i][j]
            for k in range(4):
                di = i + dr[k]
                dj = j + dc[k]
                # 최대 인덱스 확인 후 주변 먹이 더하기
                if (0 <= di < N) and (0 <= dj < N):
                    current_feed += matrix[di][dj]
            # 양수인 경우
            if current_feed > 0:
                if max_feed < current_feed:
                    max_feed = current_feed
            # 음수인 경우
            elif current_feed < 0:
                # 절댓값 구하기
                abs_max = -max_feed
                abs_current = -current_feed
                # 음수, 양수가 섞인 경우 양수인 것만 선택
                if max_feed > 0:
                    pass
                elif abs_max > abs_current:
                    max_feed = current_feed

    print(f'#{tc} {max_feed}')

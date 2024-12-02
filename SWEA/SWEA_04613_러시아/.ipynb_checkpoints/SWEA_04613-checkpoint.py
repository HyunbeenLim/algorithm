T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    
    # 국기를 같은색으로 칠한다면 행 별 해당 색으로 칠해야 하는 숫자
    paint_white = []
    paint_blue = []
    paint_red = []
    
    for row in flag:
        w_cnt = 0
        b_cnt = 0
        r_cnt = 0
        for i in range(M):
            if row[i] == 'W':
                w_cnt += 1
            elif row[i] == 'B':
                b_cnt += 1
            else:
                r_cnt += 1
        paint_white.append(b_cnt + r_cnt)
        paint_blue.append(w_cnt + r_cnt)
        paint_red.append(w_cnt + b_cnt)
    
    min_cnt = float('inf')
    # 최소 조합 찾기
    for w in range(1, N - 1): # 슬라이싱 인덱스로 활용
        for b in range(w + 1, N):
            # 첫 줄은 흰 색, 마지막 줄은 빨간 색 고정
            paint_cnt = sum(paint_white[:w]) + sum(paint_blue[w:b]) + sum(paint_red[b:])
            if paint_cnt < min_cnt:
                min_cnt = paint_cnt
            
    print(f'#{tc} {min_cnt}')
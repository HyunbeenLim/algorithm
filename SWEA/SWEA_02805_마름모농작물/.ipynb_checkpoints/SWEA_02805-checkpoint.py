import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_02805_마름모농작물/input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 항상 홀수
    farm_land = [list(map(int, input())) for _ in range(N)]
    # 중간 값
    center = N // 2

    total_profit = 0
    # r과 중간값만 활용
    for r in range(center + 1): # r: 0 -> center
        row = farm_land[r]
        profit_arr = row[(center - r):(center + r + 1)]
        for profit in profit_arr:
            total_profit += profit
        # r이 중간값이 아닐 땐 아래쪽도 더해줘야 한다
        if r != center:
            row_2 = farm_land[N - r - 1]
            profit_arr = row_2[(center - r):(center + r + 1)]
            for profit in profit_arr:
                total_profit += profit

    print(f'#{tc} {total_profit}')
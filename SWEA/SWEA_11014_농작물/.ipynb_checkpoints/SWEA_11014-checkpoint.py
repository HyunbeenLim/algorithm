import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11014_농작물/sample_input.txt', 'r')

T = int(input())

# 구간 별 수확량 함수
def harvest(sr, sc, er, ec):
    amount = 0
    for r in range(sr, er):
        for c in range(sc, ec):
            amount += farm_land[r][c]
    return amount

for tc in range(1, T + 1):
    N = int(input())
    farm_land = [list(map(int, input().split())) for _ in range(N)]
    minimum_diff = float('inf')

    for i in range(1, N):
        for j in range(1, N):
            harvest_list = [harvest(0, 0, i, j), harvest(i, 0, N, j), harvest(0, j, N, N)]
            # 농지 별 최대, 최소 수확량
            min_harvest = harvest_list[0]
            max_harvest = harvest_list[0]
            for idx in range(1, 3):
                if harvest_list[idx] > max_harvest:
                    max_harvest = harvest_list[idx]
                elif harvest_list[idx] < min_harvest:
                    min_harvest = harvest_list[idx]
            # 케이스 별 최대 수확량 - 최소 수확량의 최소값 구하기
            diff = max_harvest - min_harvest
            if diff < minimum_diff:
                minimum_diff = diff

    print(f'#{tc} {minimum_diff}')



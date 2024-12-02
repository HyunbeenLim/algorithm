import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
from itertools import combinations

# 최솟값 업데이트 함수
def update_min(indices):
    global min_dist
    
    temp_min = 0
    
    for house in dist_mat:
        distance_list = [house[idx] for idx in indices]
        temp_min += min(distance_list)
        # 더하는 중간에 현재 최솟값보다 커지면 멈추기
        if temp_min > min_dist:
            return
    # 업데이트 된 후, 전체 최솟값과 비교 후 업데이트
    else:
        if min_dist > temp_min:
            min_dist = temp_min

# T는 테스트용 
T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    field = [list(map(int, input().split())) for _ in range(N)]
    
    # 집과 치킨집의 좌표 담는 리스트
    houses = []
    restaurants = []
    
    # 거리 행렬 구할 때 쓴다
    house_cnt = 0   # 행 개수
    rest_cnt = 0    # 열 개수
    
    for r in range(N):
        for c in range(N):
            if field[r][c] == 1:
                house_cnt += 1
                houses.append((r, c))
            elif field[r][c] == 2:
                rest_cnt += 1
                restaurants.append((r, c))
    
    # 거리 행렬
    dist_mat = [[0] * rest_cnt for _ in range(house_cnt)]
    
    for r in range(house_cnt):
        for c in range(rest_cnt):
            dist_mat[r][c] = abs(houses[r][0] - restaurants[c][0]) + abs(houses[r][1] - restaurants[c][1])
    
    # 생존할 M개의 치킨집 선택
    rest_idx = list(range(rest_cnt))
    M_restaurants = list(combinations(rest_idx, M))
    
    min_dist = N ** 2 * house_cnt
    
    for survived in M_restaurants:
        update_min(survived)
    
    print(f'#{tc} {min_dist}')
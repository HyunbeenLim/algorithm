import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_09280_진용이네/sample_input.txt', 'r')

from collections import deque

# 빈 자리 내놓는 함수
def find_place():
    for i in range(1, N + 1):
        if not parking[i]:
            return i
    else:
        return False

def parking_status(car_idx):
    global parking, profit, q

    # 양수가 입력되면 요금 더해주기
    if car_idx > 0:
        car_in = car_idx
        # 앞에서부터 빈 자리 찾기
        empty_idx = find_place()
        # 빈자리가 있다면
        if empty_idx:
            # 주차하기
            parking[empty_idx] = car_in
            # 요금 계산
            profit += fee[empty_idx] * cars[car_in]
        # 빈 자리가 없을 때
        else:
            q.append(car_idx)

    else:
    # 아니면 주차공간 비워주고, 기다리는 차가 있으면 계산
        car_out = -(car_idx)
        parking[parking.index(car_out)] = 0
        if q:
            car_in = q.popleft()
            empty_idx = find_place()
            parking[empty_idx] = car_in
            profit += fee[empty_idx] * cars[car_in]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    parking = [0] * (N + 1)             # 주차공간, visited로 활용
    fee = [0] * (N + 1)                 # 무게 당 요금
    for i in range(1, N + 1):
        fee[i] = int(input())

    cars = [0] * (M + 1)                # 차 무게
    for j in range(1, M + 1):
        cars[j] = int(input())
    
    q = deque()
    profit = 0                          # 계산
    for _ in range(2 * M):
        parking_status(int(input()))

    print(f'#{tc} {profit}')
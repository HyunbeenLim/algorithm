import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11650_피자굽기/sample_input.txt', 'r')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 오븐 덱
    oven = deque()
    # 차례를 기다리는 피자 덱
    waiting_pizzas = deque(list(map(int, input().split())))
    # 피자 번호 덱
    pizza_in_oven = deque()
    pizza_number = deque(list(range(1, M + 1)))

    # 일단 오븐에 피자 N개 넣기
    for _ in range(N):
        oven.append((waiting_pizzas.popleft()) // 2)
        pizza_in_oven.append(pizza_number.popleft())

    while len(oven) > 1:
        # 1번 위치의 피자 치즈가 다 녹았으면 꺼내고 대기 피자 넣기
        # 번호 덱도 똑같이
        if oven[0] == 0:
            oven.popleft()
            pizza_in_oven.popleft()
            # 대기 피자가 없는 경우 고려하기
            if waiting_pizzas:
                oven.append((waiting_pizzas.popleft()) // 2)
                pizza_in_oven.append(pizza_number.popleft())
        # 아니라면 다음 차례를 위해 치즈 반 녹이고 뒤로 보내기
        else:
            oven.append((oven.popleft()) // 2)
            pizza_in_oven.append(pizza_in_oven.popleft())

    # while문이 종료 되었으면 오븐엔 피자 하나가 남아있다
    print(f'#{tc}', *pizza_in_oven)
import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11623_숫자카드/sample_input.txt', 'r')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = deque(list(range(1, N + 1)))

    for _ in range(len(cards) - 1):
        cards.popleft()
        sec_card = cards.popleft()
        cards.append(sec_card)

    print(f'#{tc}', *cards)


## 현이 선형 큐
t = int(input())

for tc in range(1, t+1):
    N = int(input())
    cq = [0] * (N * 2) #여유로운 Q 사이즈

    front = -1
    rear = -1 # Q초기화

    for i in range(1, N+1):
        rear += 1
        cq[rear] = i

    for _ in range(N-1):
        #deQ 두번, enQ 1번
        front += 2  # 큐의 front를 증가시켜 원소를 제거
        rear += 1   # 큐의 rear를 증가시켜 새로운 원소 추가
        cq[rear] = cq[front]  # front의 다음 원소를 rear에 추가

    print(f'#{tc} {cq[rear]}')


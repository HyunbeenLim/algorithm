import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11649_회전/sample_input.txt', 'r')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    numbers = deque(list(map(int, input().split())))
    for _ in range(M):
        numbers.append(numbers.popleft())

    print(f'#{tc} {numbers[0]}')
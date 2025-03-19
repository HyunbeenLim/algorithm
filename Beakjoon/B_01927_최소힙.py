import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
import heapq

N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            min_value = heapq.heappop(heap)
            print(min_value)
    else:
        heapq.heappush(heap, x)
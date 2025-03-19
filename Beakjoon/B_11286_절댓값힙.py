import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

import heapq

N = int(input())
arr = []
sign = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if not arr:
            print(0)
        else:
            min_abs = heapq.heappop(arr)[1]
            print(min_abs)
    else:
        heapq.heappush(arr, (abs(x), x))

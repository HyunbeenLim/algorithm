import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

import heapq

N = int(input())

arr = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if not arr:
            print(0)
        else:
            max_value = -heapq.heappop(arr)
            print(max_value)
    else:
        heapq.heappush(arr, -x)
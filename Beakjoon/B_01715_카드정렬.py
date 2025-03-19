import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

import heapq

N = int(input())
arr = []

for _ in range(N):
    heapq.heappush(arr, int(input()))

current = 0

if N > 1:
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        new_comp = first + second
        current += new_comp

        heapq.heappush(arr, new_comp)

print(current)
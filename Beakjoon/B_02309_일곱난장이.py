import sys
from itertools import combinations
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

heights = [int(input()) for _ in range(9)]
combs = combinations(heights, 7)
print_list = []
for comb in combs:
    if sum(comb) == 100:
        for height in comb:
            print_list.append(height)
        break
print_list.sort()
for height in print_list:
    print(height)
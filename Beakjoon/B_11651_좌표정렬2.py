import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

coord = []

for _ in range(N):
    a, b = map(int, input().split())
    coord.append((b, a))

coord.sort()

for xy in coord:
    a, b = xy
    print(b, a)
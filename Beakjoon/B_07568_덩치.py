import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

sizes = []
order = [1] * N

for _ in range(N):
    a, b = map(int, input().split())
    sizes.append((a, b))

for i in range(N):
    a, b = sizes[i]
    for j in range(N):
        if i == j:
            continue
        c, d = sizes[j]

        if a < c and b < d:
            order[i] += 1

print(*order)
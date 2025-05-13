import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠 주문
shirt_pack = 0

for size in sizes:
    if size % T == 0:
        shirt_pack += size // T
    else:
        shirt_pack += size // T + 1

print(shirt_pack)

# 펜
pen_pack = N // P
pens = N % P

print(pen_pack, pens)
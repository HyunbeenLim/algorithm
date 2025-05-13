import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())
count = [0] * 10001

for _ in range(N):
    idx = int(input())
    count[idx] += 1


for i in range(1, 10001):
    for _ in range(count[i]):
        sys.stdout.write(f"{i}\n")
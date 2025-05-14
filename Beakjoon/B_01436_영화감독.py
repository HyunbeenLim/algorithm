import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

idx = 1
current = 665

while idx <= N:
    current += 1
    if '666' in str(current):
        idx += 1

print(current)
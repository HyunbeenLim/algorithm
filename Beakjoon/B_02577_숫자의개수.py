import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

a = int(input())
b = int(input())
c = int(input())

count = [0] * 10

mult = str(a*b*c)

for s in mult:
    count[int(s)] += 1

for cnt in count:
    print(cnt)
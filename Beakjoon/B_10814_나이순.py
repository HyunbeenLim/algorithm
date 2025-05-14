import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

age = [[] for _ in range(201)]

for _ in range(N):
    a, b = map(str, input().split())
    age[int(a)].append(b)

for i in range(201):
    if age[i]:
        for user in age[i]:
            print(i, user)
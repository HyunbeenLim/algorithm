import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

'''
거리를 이진 탐색하라고 한다
'''
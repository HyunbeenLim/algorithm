import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

L = int(input())
string = input().strip()

r, M = 31, 1234567891

H = 0
for i in range(len(string)):
    H += (ord(string[i]) - 96) * (r ** i)

print(H % M)
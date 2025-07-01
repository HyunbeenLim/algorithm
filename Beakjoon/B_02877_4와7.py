import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

K = int(input())

binary = list(format(K+1, 'b'))
binary = binary[1:]

ans = ''

for ele in binary:
    if ele == '0':
        ans += '4'
    else:
        ans += '7'

print(ans)
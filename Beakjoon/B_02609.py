import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

a, b = map(int, input().split())

# 최대공약수
max_div = min(a, b)
a_port = a
b_port = b

while max_div > 0:
    if (a % max_div == 0) and (b % max_div == 0):
        a_port = a // max_div
        b_port = b // max_div
        break
    max_div -= 1

print(max_div)
# 최소공배수
if a_port == b_port:
    print(max_div * a_port)
else:
    print(max_div * a_port * b_port)
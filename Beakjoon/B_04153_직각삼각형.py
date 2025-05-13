import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

while True:
    tri = list(map(int, input().split()))

    if tri == [0, 0, 0]:
        break

    tri.sort()
    
    rest = 0
    for i in range(2):
        rest += tri[i] ** 2

    if tri[2] ** 2 == rest:
        print('right')
    else:
        print('wrong')
    

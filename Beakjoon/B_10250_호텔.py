import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):
    H, W, N = map(int, input().split())

    room = 1
    floor = 1
    N -= 1

    while N > 0:
        floor += 1
        if floor > H:
            floor = 1
            room += 1
        N -= 1

    ans = str(floor)
    if room >= 10:
        ans += str(room)
    else:
        ans += '0' + str(room)
    
    print(ans)
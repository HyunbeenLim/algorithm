import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_01284_수도요금경쟁/input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    a_price = P * W
    if W <= R:
        b_price = Q
    else:
        b_price = Q + (W - R) * S
    
    print(f'#{tc} {min(a_price, b_price)}')
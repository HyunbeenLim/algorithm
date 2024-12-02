import sys
sys.stdin = open('./input.txt', 'r')

T = int(input())

for tc in range(1,  T + 1):
    N, M = map(int, input().split())
    
    ans = 'ON'
    for _ in range(N):
        if M & 0b1 == 0:
            ans = 'OFF'
        M = M >> 1
    
    print(f'#{tc} {ans}')
    


#### 교수님 코드

T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    mask = (1 << N) - 1
    if (M & mask) ^ mask:
        print(f'#{test_case} OFF')
    else:
        print(f'#{test_case} ON')
import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_01860_붕어빵/input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split())) 
    
    # 정렬
    for i in range(N-1, 0, -1):
        for j in range(i):
            if customers[j] > customers[j + 1]:
                customers[j], customers[j + 1] = customers[j + 1], customers[j]
    
    bread_cnt = 0
    
    ans = 'Possible'
    
    # 손님이 올 때 붕어빵이 준비됐는지 확인하자
    for i in range(N):
        bread_cnt = (customers[i] // M) * K
        
        # 준비된 붕어빵보다 누적 손님 수가 많으면 impossible
        if bread_cnt < (i + 1):
            ans = 'Impossible'
            break
               
    print(f'#{tc} {ans}')
import sys
sys.stdin = open('sample_input.txt', 'r')

def count(a, b, n):
    big = max(a, b)
    small = min(a, b)
    
    cnt = 0
    while True:
        # 작은 수에 큰 수를 먼저 더해줘야 숫자 두개가 모두 커진 상태로 시작
        small += big
        cnt += 1
        if small > n:
            return cnt
        big += small
        cnt += 1
        if big > n:
            return cnt

T = int(input())
ans_list = []
for _ in range(T):
    x, y, N = map(int, input().split())
    ans_list.append(count(x, y, N))
    
for ans in ans_list:
    print(ans)
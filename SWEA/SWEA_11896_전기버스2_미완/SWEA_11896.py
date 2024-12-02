import sys
sys.stdin = open('./sample_input.txt', 'r')

def back_track(level, status, count):   # level은 단계를 나타낸다
    global min_charge

    # 더 이상 갈 수 없으면 멈추기
    if status == 0:
        return
    
    # 이미 count가 최소 횟수를 넘었다면 멈추기
    if count > min_charge:
        return
    
    # N에 도달했거나, 더 이상 충전하지 않아도 되면 최소 충전 횟수와 비교 후 return
    if level + status >= N or level == N:
        if min_charge > count:
            min_charge = count
        return
    
    # 충전한다
    back_track(level + 1, status - 1 + charge[level + 1], count + 1)
    # 안한다
    back_track(level + 1, status - 1, count)

T = int(input())

for tc in range(1, T + 1):
    N, *charge = list(map(int, input().split()))

    charge  = [0] + charge + [0]

    min_charge = N
    back_track(1, charge[1], 0)

    print(f'#{tc} {min_charge}')
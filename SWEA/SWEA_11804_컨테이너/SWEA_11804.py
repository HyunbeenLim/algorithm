import sys
sys.stdin = open('./sample_input.txt', 'r')

def cal(truck):
    global weights
    ans = 0
    temp_list = [x for x in weights if x <= truck]
    if temp_list:
        container_to_move = max(temp_list)
        temp_idx = weights.index(container_to_move)
        weights.pop(temp_idx)
        ans = container_to_move
    return ans 

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    weights = list(map(int, input().split()))
    limit = list(map(int, input().split()))

    max_weight = 0

    for truck in limit:
        max_weight += cal(truck)
    
    print(f'#{tc} {max_weight}')
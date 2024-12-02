T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    LR_list = []
    
    for _ in range(Q):
        LR_list.append(tuple(map(int, input().split())))
        
    for i in range(1, Q + 1):
        LR_i = LR_list.pop(0)
        L_i = LR_i[0]
        R_i = LR_i[1]
        for m in range(L_i - 1, R_i):
            boxes[m] = i
    
    print(f'#{tc}', *boxes)
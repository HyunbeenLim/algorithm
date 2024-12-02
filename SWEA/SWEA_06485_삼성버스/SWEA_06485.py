T = int(input())

for tc in range(1, T + 1):
    # 버스 노선 수
    N = int(input())

    A = []
    B = []

    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    P = int(input())
    c_list = []
    for _ in range(P):
        c_list.append(int(input())) # 나중에 인덱스 역할
            
    p_list = [0] * 5000
    
    for i in range(N):
        A_i = A[i]
        B_i = B[i]
        for j in range((A_i - 1), B_i):
            p_list[j] += 1
    
    list_to_print = []
    for c in c_list:
        list_to_print.append(p_list[c - 1])
    
    print(f'#{tc}', end = ' ')
    print(*list_to_print)
    
    
    

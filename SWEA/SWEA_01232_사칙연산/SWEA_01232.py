import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_01232_사칙연산/input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    
    for _ in range(N):
        input_values = input().split()
        
        # 정수
        if len(input_values) == 2:
            tree[int(input_values[0])] = int(input_values[1])
        # 연산자
        else:
            tree[int(input_values[0])] = [input_values[1], int(input_values[2]), int(input_values[3])]
    
    # 계산
    for i in range(N, 0, -1):
        if type(tree[i]) == list:
            operator = tree[i][0]
            c1 = tree[i][1]
            c2 = tree[i][2]
            if operator == '+':
                tree[i] = tree[c1] + tree[c2]
            elif operator == '-':
                tree[i] = tree[c1] - tree[c2]
            elif operator == '*':
                tree[i] = tree[c1] * tree[c2]
            elif operator == '/':
                tree[i] = tree[c1] // tree[c2]
                
    print(f'#{tc} {tree[1]}')

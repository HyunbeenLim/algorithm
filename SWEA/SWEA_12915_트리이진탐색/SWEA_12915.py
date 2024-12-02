import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_12915_트리이진탐색/sample_input.txt', 'r')

def inorder(v):
    global tree
    
    if v == 0: return
    
    inorder(left[v])
    # 노드 번호
    tree.append(v)
    inorder(right[v])

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    
    # 부모 - 자식 넣어주기
    for i in range(2, N + 1):
        if i % 2 == 0:
            left[i//2] = i
        else:
            right[i//2] = i
    
    # 트리 - 중위탐색 순서에 따른 노드 탐색 순서
    tree = [0] 
    
    inorder(1)
    
    # 완전이진트리로 재배치 한다면 현재 트리에서 인덱스 가져오면 된다!
    root = tree.index(1)
    center = tree.index(N//2)
    
    print(f'#{tc} {root} {center}')
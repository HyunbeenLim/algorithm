import sys; sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/07 Tree/tree_input.txt')

V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

arr = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    # p(부모)를 인덱스로 사용
    # 먼저 나온 걸 왼쪽에 넣기
    # 왼쪽에 이미 있다면 오른쪽
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

print('중위순회')
def inorder(v):
    if v == 0: return
    inorder(L[v])
    print(v, end=' ') # 얘만 쓰면 inorder
    inorder(R[v])

inorder(1)
print()
print('전위순회')
def preorder(v):
    if v == 0: return
    print(v, end=' ')
    preorder(L[v])
    preorder(R[v])

preorder(1)
print()
print('후위순회')
def postorder(v):
    if v == 0: return
    postorder(L[v])
    postorder(R[v])
    print(v, end=' ')

postorder(1)
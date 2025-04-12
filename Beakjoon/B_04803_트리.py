import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

# find
def find_root(x):
    global root

    if root[x] != x:
        root[x] = find_root(root[x])

    return root[x]

# union
def union(x, y):    # 앞의 노드를 루트로 가정
    global cycle_set

    x_root = find_root(x)
    y_root = find_root(y)

    if x_root != y_root:
        if x_root in cycle_set or y_root in cycle_set:
            # 사이클이 있는 집합이 트리인 집합과 연결되면, 트리인 집합도 사이클 집합에 포함되어 더 이상 트리가 아님
            cycle_set.add(x_root)
            cycle_set.add(y_root)
        else:
            root[y_root] = x_root
    elif x_root == y_root:
        # 이미 루트 노드가 같은 두 노드를 연결한다면 사이클이 생김
        cycle_set.add(x_root)

case = 1
while True:
    nodes, edges = map(int, input().split())

    if (nodes, edges) == (0, 0):
        break

    root = []
    for i in range(nodes+1):
        root.append(i)

    cycle_set = set()

    for _ in range(edges):
        v1, v2 = map(int, input().split())
        union(v1, v2)

    # 루트 개수 세기
    all_roots = set(find_root(i) for i in range(1, nodes+1))
    # 사이클이 존재하는 집합 제거
    tree_roots = all_roots - cycle_set
    # 트리 개수 세기
    tree_cnt = len(tree_roots)

    if tree_cnt == 0:
        ans = 'No trees.'
    elif tree_cnt == 1:
        ans = 'There is one tree.'
    else:
        ans = f'A forest of {tree_cnt} trees.'

    print(f'Case {case}: {ans}')
    case += 1
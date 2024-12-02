def dfs(s):
    visited = [0] * 100
    stack = []
    visited[s] = 1
    v = s
    while True:
        for w in g[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return visited
        
for j in range(1, 11):
    tc, v = map(int, input().split()) # test case, 노드
    g = [[] for _ in range(100)] # 인접 리스트
    
    edge_list = list(map(int, input().split()))
    list_half_length = int(len(edge_list)/2)
    
    for i in range(list_half_length):
        # 길이 반만 반복
        v1, v2 = edge_list[2*i], edge_list[2*i + 1]
        g[v1].append(v2)
    
    visited = dfs(0)
    
    if visited[99]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
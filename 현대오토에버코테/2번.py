def solution(n, networks, server_pair):
    edges = [[0] * (n + 1) for _ in range(n+1)]

    for network in networks:
        node_a, node_b, cost = network

        if edges[node_a][node_b] == 0:
            edges[node_a][node_b] = [cost]
        else:
            edges[node_a][node_b].append(cost)

        if edges[node_b][node_a] == 0:
            edges[node_b][node_a] = [cost]
        else:
            edges[node_b][node_a].append(cost)

    max_cost = 0
    min_cost = 0

    visited = set(range(1, n+1))
    
    for pair in server_pair:
        node_a, node_b = pair

        max_cost += max(edges[node_a][node_b])
        min_cost += min(edges[node_a][node_b])

        if node_a in visited:
            visited.remove(node_a)
        if node_b in visited:
            visited.remove(node_b)

    for left in visited:
        left_node = edges[left]
        current_min = 10001
        current_max = -1
        for costs in left_node:
            if costs:
                current_min = min(current_min, min(costs))
                current_max = max(current_max, min(costs))
        max_cost +=  current_max
        min_cost += current_min

    return [min_cost, max_cost]

print(solution(4, [[1, 2, 30], [2, 3, 100], [2, 3, 2000], [3, 4, 20]], [[1, 2], [2, 3]]))


### 정답 코드
def solution(n, networks, server_pair):
    costs_by_pair = {}

    for a, b, c in networks:
        if a > b:
            a, b = b, a
        costs_by_pair.setdefault((a, b), []).append(c)

    def calc(is_min):
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
            return True

        total = 0
        used_edges = 0
        required_pairs = set()

        # 필수 direct edge 선택
        for a, b in server_pair:
            if a > b:
                a, b = b, a
            required_pairs.add((a, b))

            arr = costs_by_pair[(a, b)]
            c = min(arr) if is_min else max(arr)

            total += c
            used_edges += 1
            union(a, b)

        # 나머지 간선
        edges = []
        for a, b, c in networks:
            x, y = (a, b) if a < b else (b, a)

            # 필수 pair의 경우 이미 direct edge 하나를 선택했으므로
            # 추가 간선은 굳이 사용할 필요 없음
            if (x, y) in required_pairs:
                continue

            edges.append((c, a, b))

        edges.sort(reverse=not is_min)

        for c, a, b in edges:
            if union(a, b):
                total += c
                used_edges += 1

        # 연결 확인
        root = find(1)
        if any(find(i) != root for i in range(2, n + 1)):
            return None

        return total

    return [calc(True), calc(False)]
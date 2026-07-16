def solution(mats, park):
    mats.sort(reverse=True)

    N = len(park)
    M = len(park[0])

    for size in mats:
        for r in range(N - size + 1):
            for c in range(M - size + 1):
                
                empty = True
                for i in range(r, r + size):
                    for j in range(c, c + size):
                        if park[i][j] != "-1":
                            empty = False
                            break
                    if not empty:
                        break
                if empty:
                    return size

    return -1



print(solution([5,3,2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))


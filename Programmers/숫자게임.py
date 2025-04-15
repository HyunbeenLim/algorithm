def solution(A, B):
    A.sort()
    B.sort()

    score = 0
    s = 0
    e = len(B) - 1

    for a in A:
        while s <= e:
            if B[s] > a:
                score += 1
                s += 1
                break
            s += 1
        if s > e:
            break

    return score


print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))
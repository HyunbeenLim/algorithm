import heapq

def solution(n, works):
    # 최대 힙 만들기
    works = [-w for w in works]
    heapq.heapify(works)

    while n > 0 and works:
        max_work = heapq.heappop(works)
        if max_work == 0:
            return 0
        heapq.heappush(works, max_work + 1)
        n -= 1

    return sum(w ** 2 for w in works)


print(solution(4, [4, 3, 3]))   # 12
print(solution(1, [2, 1, 2]))   # 6
print(solution(3, [1,1]))       # 0
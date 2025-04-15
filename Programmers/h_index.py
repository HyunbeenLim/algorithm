def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    else:
        return len(citations)
    

print(solution([3, 0, 6, 1, 5]))
print(solution([5, 6, 7, 8]))
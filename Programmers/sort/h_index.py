def solution(citations):
    citations.sort()

    h_index = 0
    for i in range(len(citations)):
        if (i <= len(citations) - i) and (h_index <= len(citations) - i) and (i < citations[i]):
            h_index = len(citations) - i

    return h_index


print(solution([3, 0, 6, 1, 5]))        # [0, 1, 3, 5, 6]
print(solution([5, 6, 7, 8]))

# 입력값 〉 [5, 6, 7, 8]
# 기댓값 〉 4
# 말이 너무 어려워ㅜㅜ 이해하고 다시 풀어보자ㅜㅜ
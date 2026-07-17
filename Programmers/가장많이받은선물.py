def solution(friends, gifts):
    # 선물 기록 행렬 만들기
    N = len(friends)
    gift_matrix = [[0] * N for _ in range(N)]

    for log in gifts:
        ele = log.split(sep = " ")
        gift_matrix[friends.index(ele[0])][friends.index(ele[1])] += 1

    # 선물 지수
    gift_index = [0] * N
    for i in range(N):
        # 준 선물
        gave = sum(gift_matrix[i])

        # 받은 선물
        got = 0
        for j in range(N):
            if j != i:
                got += gift_matrix[j][i]
        gift_index[i] = gave - got

    # 받을 선물
    planned = [0] * N
    for i in range(N):
        cnt = 0
        for j in range(N):
            if gift_matrix[i][j] > gift_matrix[j][i]:
                cnt += 1
            elif gift_matrix[i][j] == gift_matrix[j][i]:
                if gift_index[i] > gift_index[j]:
                    cnt += 1
        planned[i] = cnt

    return max(planned)



print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))

### 챗 gpt 코드

def solution(friends, gifts):
    n = len(friends)

    # 이름 → 인덱스
    friend_idx = {
        name: i
        for i, name in enumerate(friends)
    }

    # gift_matrix[i][j]:
    # i가 j에게 준 선물 개수
    gift_matrix = [[0] * n for _ in range(n)]

    # 준 선물 수 - 받은 선물 수
    gift_index = [0] * n

    for gift in gifts:
        giver, receiver = gift.split()

        giver_idx = friend_idx[giver]
        receiver_idx = friend_idx[receiver]

        gift_matrix[giver_idx][receiver_idx] += 1
        gift_index[giver_idx] += 1
        gift_index[receiver_idx] -= 1

    # 다음 달에 받을 선물 수
    planned = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if gift_matrix[i][j] > gift_matrix[j][i]:
                planned[i] += 1

            elif gift_matrix[i][j] < gift_matrix[j][i]:
                planned[j] += 1

            else:
                if gift_index[i] > gift_index[j]:
                    planned[i] += 1
                elif gift_index[i] < gift_index[j]:
                    planned[j] += 1

    return max(planned)

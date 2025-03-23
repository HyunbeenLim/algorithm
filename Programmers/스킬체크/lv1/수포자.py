def solution(answers):
    ans = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            cnt_1 += 1
        if answers[i] == second[i%8]:
            cnt_2 += 1
        if answers[i] == third[i%10]:
            cnt_3 += 1

    cnt_lst = [0, cnt_1, cnt_2, cnt_3]
    max_cnt = max(cnt_lst)

    for i in range(len(cnt_lst)):
        if cnt_lst[i] == max_cnt:
            ans.append(i)

    return ans

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
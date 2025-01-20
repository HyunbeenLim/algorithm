'''
1번 -> 1, 2, 3, 4, 5 반복
2번 -> 2, 1, 2, 3, 2, 4, 2, 5 반복
3번 -> 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복 
'''

def solution(arr):
    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    for i in range(len(arr)):
        correct_ans = arr[i]

        ans_1 = arr_1[i % 5]
        ans_2 = arr_2[i % 8]
        ans_3 = arr_3[i % 10]

        if ans_1 == correct_ans:
            cnt_1 += 1
        if ans_2 == correct_ans:
            cnt_2 += 1
        if ans_3 == correct_ans:
            cnt_3 += 1
    
    correct_cnt = [0, cnt_1, cnt_2, cnt_3]
    max_cnt = max(correct_cnt)

    ans = [i for i in range(4) if correct_cnt[i] == max_cnt]

    return ans

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
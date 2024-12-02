import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12392/sample_input.txt", "r")
# input = sys.stdin.readline

# 정렬 함수 - 카운팅 정렬 - 수업시간에 했음 나중에 이해해도 됨
def counting_sort(arr):
    n = len(arr)
    
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    counts = [0] * (max_value + 1)
    for ele in arr:
        counts[ele] += 1

    adj_counts = [0] * (max_value + 1)
    adj_counts[0] = counts[0]

    for i in range(1, max_value + 1):
        adj_counts[i] = adj_counts[i - 1] + counts[i]

    sorted_list = [0] * n
    for j in range(n - 1, -1, -1):  
        element = arr[j]
        adj_counts[element] -= 1
        sort_idx = adj_counts[element]
        sorted_list[sort_idx] = element

    return sorted_list

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # input 숫자 리스트
    number_list = list(map(int, input().split()))
    
    # 위에 정의한 함수로 리스트 정렬 => 나중엔 sorted() 써도 됨
    sorted_list = counting_sort(number_list)
    
    # 빈 리스트 -> 문제에서 요구하는 리스트 만들기
    ans = []
    
    # 최소, 최대 인덱스 정의 -> sorted_list의 인덱스로 활용 됨
    min_idx = 0
    max_idx = n - 1
    
    # 최소, 최대 인덱스 조정하기 위해 while 문 사용
    ## 첫번째 반복: 리스트에서 가장 크고 작은 원소들을 할당
    ## 두번째 반복: 두번째로 크고 작은 원소들을 할당
    ## 반복
    while min_idx <= 4: # 이 문제는 길이 10의 제한이 있어서 min_idx < 4로 했지만, 그 제한이 없으면 while min_idx <= end_idx로 하는게 맞다
        ans.append(sorted_list[max_idx])
        ans.append(sorted_list[min_idx])
    
        # 인덱스 업데이트
        max_idx -= 1
        min_idx += 1
    
    print(f'#{tc}', *ans)





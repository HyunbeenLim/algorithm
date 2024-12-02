import sys
sys.stdin = open('sample_input.txt', 'r')
from itertools import combinations

# 식재료 조합 별 맛 구하기:
def cal_taste(lst):
    taste = 0

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            taste += matrix[lst[i]][lst[j]]
            taste += matrix[lst[j]][lst[i]]
    
    return taste

# 맛의 차이 구하기
def cal_diff(indices):
    global min_diff

    set_1 = list(indices)
    set_2 = [x for x in list(range(N)) if x not in set_1]
    
    taste_1 = cal_taste(set_1)
    taste_2 = cal_taste(set_2)

    min_diff = min(min_diff, abs(taste_1 - taste_2))


for tc in range(1, int(input()) + 1):
    N = int(input())

    matrix = []
    
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    combi = list(combinations(list(range(N)), N//2))
    
    min_diff = float('inf')

    # 중복 제거
    for comb in combi[:len(combi)//2]:
        cal_diff(comb)
    
    print(f'#{tc} {min_diff}')

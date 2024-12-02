import sys
input = sys.stdin.readline

N = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)
adjusted_score = list(map(lambda x : x / max_score * 100, score_list))
adjusted_mean = sum(adjusted_score) / len(adjusted_score)
print(adjusted_mean)
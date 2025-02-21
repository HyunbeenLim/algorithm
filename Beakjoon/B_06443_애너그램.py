import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

'''
중복된 알파벳이 존재할 때 중복을 막기 위해 word_set을 사용해도 탐색 자체는 못 막기 때문에 시간 초과가 발생
딕셔너리를 사용한다면 visited, word_set을 사용할 필요 없이 중복 탐색을 하지 않는다
'''

def make_words(ans):
    if len(ans) == len(input_word):
        print(ans)
        return
        
    for alphabet in alphabet_cnt:
        if alphabet_cnt[alphabet]:
            alphabet_cnt[alphabet] -= 1
            make_words(ans+alphabet)
            alphabet_cnt[alphabet] += 1

N = int(input())

for _ in range(N):
    input_word = list(input().rstrip())
    input_word = sorted(input_word)

    alphabet_cnt = {}

    for alphabet in input_word:
        if alphabet in alphabet_cnt:
            alphabet_cnt[alphabet] += 1
        else:
            alphabet_cnt[alphabet] = 1

    make_words('')



########## 시간 초과된 코드 ###########

# def make_words(idx):
#     if idx == len(input_word):
#         string = ''.join(arr)
#         if string not in word_set:
#             word_set.add(string)
#             print(string)
#             return
        
#     for i in range(len(input_word)):
#         if visited[i]:
#             continue
#         arr[idx] = input_word[i]
#         visited[i] = 1
#         make_words(idx+1)
#         visited[i] = 0

# N = int(input())

# for _ in range(N):
#     input_word = list(input().rstrip())
#     input_word = sorted(input_word)

#     visited = [0] * len(input_word)
#     arr = [0] * len(input_word)
#     word_set = set()

#     make_words(0)
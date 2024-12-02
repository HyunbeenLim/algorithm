import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_01221/GNS_test_input.txt", "r")

T = int(input())

numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T + 1):
    input_string = input()

    # 굳이 이걸 빼낼 필요가 있나 싶음
    for i in range(len(input_string)):
        if input_string[i] == ' ':
            word_num = int(input_string[i + 1:])
            break
    
    # 빈도수 확인
    count_list = [0] * 10
    word_string = input()
    # 단어 시작, 끝 지점
    word_start = 0
    word_end = 3

    while word_end <= len(word_string):
        num = word_string[word_start:word_end]

        # 해당 위치의 문자열이 numbers에 포함되어 있다면 count_list의 해당 인덱스에 +1
        for i in range(10):
            if numbers[i] == num:
                count_list[i] += 1
        
        word_start += 4
        word_end += 4

    string_to_print = str()
    for i in range(10):
        string_to_print += (numbers[i] + ' ') * count_list[i]
    
    print(f'#{tc}')
    print(string_to_print)
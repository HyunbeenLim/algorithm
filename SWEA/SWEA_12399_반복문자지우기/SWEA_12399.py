import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12399_반복문자지우기/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    string = input()

    stack = [0] * len(string)
    top = -1

    for char in string:
        # 비어있으면  push
        if top == -1:
            top += 1
            stack[top] = char
        # 다음 문자열과 top에 있는 문자열이 같으면 pop
        elif char == stack[top]:
            top -= 1
        # 다르면 push
        elif char != stack[top]:
            top += 1
            stack[top] = char
    
    # 남은 문자열의 길이는 top + 1
    print(f'#{tc} {top + 1}')
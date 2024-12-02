# 입력받은 알파벳을 비트로 바꿔주기
def alpha_to_bit(alphabet):
    arr = []
    number = ord(alphabet)

    start = 6
    while start != -1:
        if number >= (2 ** start):
            arr.append(1)
            number -= 2 ** start
        else:
            arr.append(0)

        start -= 1

    return arr

# 노드가 7개인 완전이진트리의 중위순회출력순서
print_order = [3, 1, 4, 0, 5, 2, 6]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    string = input()
    
    # 출력 형식에 맞춰 출력
    print(f'#{tc}', end = ' ')
    for alpha in string:
        ans = ''
        ans_arr = alpha_to_bit(alpha)
        for idx in print_order:
            ans += str(ans_arr[idx])
        print(ans, end = ' ')
    print()
    
    
# 교수님 비트 만드는 코드
# arr = input()
# for ch in arr:
#     val = ord(ch)
#     bin_str = ''
#     for i in range(6, -1, -1):
#         if val & (1 << i):
#             bin_str += '1'
#         else:
#             bin_str += '0'
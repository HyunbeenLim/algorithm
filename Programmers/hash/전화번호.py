########### 수정 전 ###########
# def solution(phone_book):
#     n = len(phone_book)
#     indices = list(range(n))

#     answer = True

#     for i in range(n):
#         current_number = phone_book[i]
#         for idx in indices:
#             number_to_compare = phone_book[idx]
#             if i == idx or len(current_number) > len(number_to_compare):     
#                 continue
#             else:
#                 fraction = number_to_compare[:len(current_number)]
#                 if current_number == fraction:
#                     answer = False

#     return answer

########### 수정 후 ###########
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
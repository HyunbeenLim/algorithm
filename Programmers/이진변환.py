def solution(string):
    convert = 0
    eliminated = 0

    while len(string) > 1:
        current_length = len(string)

        count_one = 0

        for s in string:
            if int(s) == 1:
                count_one += 1
        
        eliminated += current_length - count_one

        new_string = ''
        while count_one > 0:
            if count_one % 2 == 0:
                new_string = '0' + new_string
            else:
                new_string = '1' + new_string
            count_one //= 2
        
        string = new_string
        convert += 1

    return [convert, eliminated]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
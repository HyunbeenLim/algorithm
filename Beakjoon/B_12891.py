import sys
input = sys.stdin.readline

def add_number(number_list:list, alpha:str):
    if alpha == 'A':
        number_list[0] += 1
    elif alpha == 'C':
        number_list[1] += 1
    elif alpha == 'G':
        number_list[2] += 1
    elif alpha == 'T':
        number_list[3] += 1
    
    return number_list

def reduce_number(number_list:list, alpha:str):
    if alpha == 'A':
        number_list[0] -= 1
    elif alpha == 'C':
        number_list[1] -= 1
    elif alpha == 'G':
        number_list[2] -= 1
    elif alpha == 'T':
        number_list[3] -= 1
    
    return number_list


str_len, pw_len = map(int, input().split())
dna_str = input()
check_list = list(map(int, input().split()))

start_idx = 0
end_idx = pw_len - 1
cnt = 0

current_str = dna_str[start_idx:end_idx]
number_list = [current_str.count('A'), current_str.count('C'), current_str.count('G'), current_str.count('T')]

while end_idx == str_len:
    for i in range(4):
        if number_list[i] < check_list[i]:
            break
        else:
            cnt += 1
        
        number_list = add_number(number_list, dna_str[end_idx])
        number_list = reduce_number(number_list, dna_str[start_idx])

        start_idx += 1
        end_idx += 1
    
print(cnt)
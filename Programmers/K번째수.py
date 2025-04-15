def find_k(arr, comm):
    i = comm[0] - 1
    j = comm[1]
    k = comm[2] - 1

    new_arr = arr[i:j]
    new_arr.sort()

    return new_arr[k]

def solution(array, commands):
    answer = []
    
    for comm in commands:
        answer.append(find_k(array, comm))
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# from itertools import combinations, permutations, product


# N = 4

# combination = list(combinations(list(range(N)), 2))
# permutation = list(permutations(list(range(N)), 2))
# prod = list(product(list(range(N)), repeat=2))

# print(f'combinations {combination}')
# print(f'permutations {permutation}')
# print(f'prod {prod}')


# combi = combinations(list(range(N)), 2)

# for comb in combi:
#     print(comb)

# w = [3,1,4,5]
# print(w)

# w = list(map(str, w))
# print(w)

# print(max(enumerate(w), key=lambda x: x[1][0]))

pascal = []

for i in range(7):
    pascal.append([1]*(i+1))

for i in range(7):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

for i in range(len(pascal)):
    print(i)
    print(pascal[i][1:(i+1)])
    print(sum(pascal[i][1:(i+1)]))
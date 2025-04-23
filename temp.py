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


N = 5

q = 0
w = 4

print((q-1)%N, (q+1)%N) # 4, 1
print((w-1)%N, (w+1)%N) # 3, 0
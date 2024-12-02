from itertools import combinations, permutations, product


N = 4

combination = list(combinations(list(range(N)), 2))
permutation = list(permutations(list(range(N)), 2))
prod = list(product(list(range(N)), repeat=2))

print(f'combinations {combination}')
print(f'permutations {permutation}')
print(f'prod {prod}')


combi = combinations(list(range(N)), 2)

for comb in combi:
    print(comb)
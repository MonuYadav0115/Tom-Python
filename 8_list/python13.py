

# permutation : means all posible to arrange value of list like how many combination of the this list 

import itertools as it 

l = ["a","b","c","d"]

permutation = it.permutations(l,r=2)

permutation_list = list(permutation)

for i in permutation_list:
    print(i)



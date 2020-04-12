from dameraulevenshtein import damerau_levenshtein_diversity, damerau_levenshtein_distance

# from timeit import timeit
# from example_py import test

# cy = timeit('test(5000)', setup='from example_cy import test', number=100)
# py = timeit('test(5000)', setup='from example_py import test', number=100)
# print(cy, py)
# print('Cython is {}x faster'.format(py/cy))



def damerau_levenshtein_diversity_py(array):
    dl_distance = 0
    n = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            dl_distance += damerau_levenshtein_distance(array[i], array[j])
    return dl_distance / (n * (n + 1) / 2)

test_list = ['123', '234', '345']
print('py diversity' , damerau_levenshtein_diversity_py(test_list))
print('c diversity', damerau_levenshtein_diversity(test_list))

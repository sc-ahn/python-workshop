import timeit
import array
import numpy as np

# params

LENGTH = 10000
ITERATION = 1000

# initialize list, array, and ndarray

my_list = [_ for _ in range(LENGTH)]
my_array = array.array('i', my_list)
my_ndarray = np.array(my_list)

def test_list_sum():
    sum(my_list)

def test_array_sum():
    sum(my_array)

def test_ndarray_sum():
    sum(my_ndarray)

def test_numpy_npsum():
    np.sum(my_ndarray)


# benchmark
list_time = timeit.timeit(test_list_sum, number=ITERATION)
array_time = timeit.timeit(test_array_sum, number=ITERATION)
ndarray_sum_time = timeit.timeit(test_ndarray_sum, number=ITERATION)
ndarray_npsum_time = timeit.timeit(test_numpy_npsum, number=ITERATION)

# result: summation
print(f'List sum time: {list_time * 1000:.1f} ms')
print(f'Array sum time: {array_time * 1000:.1f} ms')
print(f'ndarray sum time: {ndarray_sum_time * 1000:.1f} ms')
print(f'ndarray npsum time: {ndarray_npsum_time * 1000:.1f} ms')

import timeit
import array
import pickle
import random
import numpy as np

LENGTH = 10000
ITERATION = 1000

my_list = [random.random() for _ in range(LENGTH)]
my_list_encoded = pickle.dumps(my_list)

my_array = array.array('f', my_list)
my_array_encoded = pickle.dumps(my_array)

my_ndarray = np.array(my_list, dtype=np.float32)
my_ndarray_encoded = pickle.dumps(my_ndarray)

def test_list_pickle():
    pickle.dumps(my_list)

def test_list_unpickle():
    pickle.loads(my_list_encoded)

def test_array_pickle():
    pickle.dumps(my_array)

def test_array_unpickle():
    pickle.loads(my_array_encoded)

def test_ndarray_pickle():
    pickle.dumps(my_ndarray)

def test_ndarray_unpickle():
    pickle.loads(my_ndarray_encoded)

# benchmark
list_pickle_time = timeit.timeit(test_list_pickle, number=ITERATION)
list_unpickle_time = timeit.timeit(test_list_unpickle, number=ITERATION)
array_pickle_time = timeit.timeit(test_array_pickle, number=ITERATION)
array_unpickle_time = timeit.timeit(test_array_unpickle, number=ITERATION)
ndarray_pickle_time = timeit.timeit(test_ndarray_pickle, number=ITERATION)
ndarray_unpickle_time = timeit.timeit(test_ndarray_unpickle, number=ITERATION)

# result
print(f"List pickle: {list_pickle_time* 1000:.1f} ms")
print(f"List unpickle: {list_unpickle_time* 1000:.1f} ms")
print(f"Array pickle: {array_pickle_time* 1000:.1f} ms")
print(f"Array unpickle: {array_unpickle_time* 1000:.1f} ms")
print(f"Numpy ndarray pickle: {ndarray_pickle_time* 1000:.1f} ms")
print(f"Numpy ndarray unpickle: {ndarray_unpickle_time* 1000:.1f} ms")

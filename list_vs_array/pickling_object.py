import timeit
import pickle
import random
import numpy as np

LENGTH = 10000
ITERATION = 1000

class DummyObject:
    def __init__(self):
        self.hello = random.random()

my_list = [DummyObject() for _ in range(LENGTH)]
my_list_encoded = pickle.dumps(my_list)

# array cannot contain object, only primitive type
# so we skip this part

my_ndarray = np.array(my_list, dtype=np.object_)
my_ndarray_encoded = pickle.dumps(my_ndarray)

def test_list_pickle():
    pickle.dumps(my_list)

def test_list_unpickle():
    pickle.loads(my_list_encoded)

def test_ndarray_pickle():
    pickle.dumps(my_ndarray)

def test_ndarray_unpickle():
    pickle.loads(my_ndarray_encoded)

# benchmark
list_pickle_time = timeit.timeit(test_list_pickle, number=ITERATION)
list_unpickle_time = timeit.timeit(test_list_unpickle, number=ITERATION)
ndarray_pickle_time = timeit.timeit(test_ndarray_pickle, number=ITERATION)
ndarray_unpickle_time = timeit.timeit(test_ndarray_unpickle, number=ITERATION)

# result

print(f"List pickle: {list_pickle_time* 1000:.1f} ms")
print(f"List unpickle: {list_unpickle_time* 1000:.1f} ms")
print(f"Numpy ndarray pickle: {ndarray_pickle_time* 1000:.1f} ms")
print(f"Numpy ndarray unpickle: {ndarray_unpickle_time* 1000:.1f} ms")

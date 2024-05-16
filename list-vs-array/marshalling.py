import timeit
import array
import marshal
import random
import numpy as np

LENGTH = 10000
ITERATION = 1000

my_list = [random.random() for _ in range(LENGTH)]
my_list_encoded = marshal.dumps(my_list)

my_array = array.array('f', my_list)
my_array_encoded = marshal.dumps(my_array)

my_ndarray = np.array(my_list, dtype=np.float32)
my_ndarray_encoded = marshal.dumps(my_ndarray)

def test_list_marshal():
    marshal.dumps(my_list)

def test_list_unmarshal():
    marshal.loads(my_list_encoded)

def test_array_marshal():
    marshal.dumps(my_array)

def test_array_unmarshal():
    marshal.loads(my_array_encoded)

def test_ndarray_marshal():
    marshal.dumps(my_ndarray)

def test_ndarray_unmarshal():
    marshal.loads(my_ndarray_encoded)

# benchmark
list_marshal_time = timeit.timeit(test_list_marshal, number=ITERATION)
list_unmarshal_time = timeit.timeit(test_list_unmarshal, number=ITERATION)
array_marshal_time = timeit.timeit(test_array_marshal, number=ITERATION)
array_unmarshal_time = timeit.timeit(test_array_unmarshal, number=ITERATION)
ndarray_marshal_time = timeit.timeit(test_ndarray_marshal, number=ITERATION)
ndarray_unmarshal_time = timeit.timeit(test_ndarray_unmarshal, number=ITERATION)

# result

print(f"List marshal: {list_marshal_time* 1000:.1f} ms")
print(f"List unmarshal: {list_unmarshal_time* 1000:.1f} ms")
print(f"Array marshal: {array_marshal_time* 1000:.1f} ms")
print(f"Array unmarshal: {array_unmarshal_time* 1000:.1f} ms")
print(f"Numpy ndarray marshal: {ndarray_marshal_time* 1000:.1f} ms")
print(f"Numpy ndarray unmarshal: {ndarray_unmarshal_time* 1000:.1f} ms")

# list VS array

## script usage

```bash
pwd # list-vs-array
poetry run python summation.py
poetry run python marshalling.py
poetry run python pickling.py
poetry run python pickling_object.py
```

## Python built-in list

[Python의 builtin-list 객체 구조체](https://github.com/python/cpython/blob/46c808172fd3148e3397234b23674bf70734fb55/Include/cpython/listobject.h#L8)

```c
typedef struct {
    PyObject_VAR_HEAD
    /* Vector of pointers to list elements.  list[0] is ob_item[0], etc. */
    PyObject **ob_item;

    /* ob_item contains space for 'allocated' elements.  The number
     * currently in use is ob_size.
     * Invariants:
     *     0 <= ob_size <= allocated
     *     len(list) == ob_size
     *     ob_item == NULL implies ob_size == allocated == 0
     * list.sort() temporarily sets allocated to -1 to detect mutations.
     *
     * Items must normally not be NULL, except during construction when
     * the list is not yet visible outside the function that builds it.
     */
    Py_ssize_t allocated;
} PyListObject;
```

포인터들의 배열로 구성되어있음.
Python에서 접근하는경우 인접 요소라고 하더라도 실제 메모리상에서는 멀리 떨어져있을 수 있음.

cache locality 저하 -> cache miss -> 성능 저하

## Python built-in array

[Python의 built-in array 객체 구조체](https://github.com/python/cpython/blob/46c808172fd3148e3397234b23674bf70734fb55/Modules/arraymodule.c#L43)

```c
typedef struct arrayobject {
    PyObject_VAR_HEAD
    char *ob_item;
    Py_ssize_t allocated;
    const struct arraydescr *ob_descr;
    PyObject *weakreflist; /* List of weak references */
    Py_ssize_t ob_exports;  /* Number of exported buffers */
} arrayobject;
```

list와 동일하게 `ob_item`을 가지지만, list의 경우 `PyObject` 타입이고 array의 경우 `char*` 타입임.

built-in array는 객체의 래퍼런스를 들고있는 것이 아니라, 값 자체를 들고있어서 locality가 보장됨.

대신 int, byte, float 등 primitive한 값만 저장할 수 있다는 제약이 있음.

## Numpy: ndarray

Numpy의 ndarray가 c로 구현되어있고 built-in array와 비슷하게 연속된 메모리 공간에 값을 할당하기에 매우 빠른 속도로 메모리 접근이 가능함.

다만 ndarray의 `dtype`을 `0` 으로 설정하는경우 값이 아닌 객체에 대한 reference를 저장하기에 built-in list와 같은 동작을함.

[class numpy.object_](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_)

```text
The data actually stored in object arrays (i.e., arrays having dtype object_) are references to Python objects, not the objects themselves. Hence, object arrays behave more like usual Python lists, in the sense that their contents need not be of the same Python type.

The object type is also special because an array containing object_ items does not return an object_ object on item access, but instead returns the actual object that the array item refers to.
```

## 성능평가: Summationn

```bash
List sum time: 77.2 ms
Array sum time: 178.3 ms
ndarray sum time: 675.6 ms
ndarray npsum time: 4.2 ms
```

모든 요소들을 한 번씩 읽고 더하는 연산을 수행했습니다.

ndarray는 np.sum()을 사용할 때 빠르지만, 내장 sum()을 사용할땐 list에 비해 느림.

array도 마찬가지로 list에 비해 느림.

array, ndarray는 python 객체가 아닌 primitive 값을 저장했기에, sum()을 실행하는 과정에서 값에 접근하려면 primitive 값을 Python 객체로 변환하는 과정이 필요함.

변환하는 과정이 오버헤드가 되어 list에 sum()을 수행하는것보다 느린 것으로 보임.

## 성능평가: Serialize

### w/ pickle

```bash
List pickle: 142.6 ms
List unpickle: 165.8 ms
Array pickle: 3.0 ms
Array unpickle: 2.5 ms
Numpy ndarray pickle: 5.8 ms
Numpy ndarray unpickle: 3.3 ms
```

### w/ marshal

```bash
List marshal: 108.0 ms
List unmarshal: 126.8 ms
Array marshal: 0.8 ms
Array unmarshal: 0.7 ms
Numpy ndarray marshal: 0.8 ms
Numpy ndarray unmarshal: 0.7 ms
```

array와 ndarray가 직렬화과정에서 list에 비해 월등히 빠른 것을 확인할 수 있음.

list의 경우 cache-locality가 떨어지기에 분산되어있는 데이터를 모으는 과정이 필요할 것이고, 데이터 타입을 확인한 뒤 바이너리로 변환하기에 오버헤드가 발생할 것으로 보임.

### w/ pickle but dtype=object

```bash
List pickle: 5539.7 ms
List unpickle: 2298.4 ms
Numpy ndarray pickle: 5208.9 ms
Numpy ndarray unpickle: 2091.1 ms
```

array는 primitive한 값만 저장할 수 있기에 이 과정에서는 제외하였음.

ndarray는 dtype이 object인 경우 list와 같은 성능을 보임.

데이터 타입을 확인한 뒤 바이트스트림으로 변환하는 과정에서 오버헤드가 발생했을 것으로 보임.

## 결론

- list는 다양한 타입을 저장할 수 있지만, cache locality가 떨어져 성능이 떨어짐.
- array는 primitive한 타입만 저장할 수 있지만, cache locality가 높아 성능이 비교적 좋음.
- ndarray는 array와 비슷하지만, 다양한 타입을 저장할 수 있음. 다만, dtype이 object인 경우 list와 비슷한 성능을 보임.

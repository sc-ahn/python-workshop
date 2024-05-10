import gc


DESCRIPTITON_1 = """
Python에서 각 객체는 generation 0-2 중 하나에 속함.
기준은 해당 객체가 cyclic garbage collector로 부터 생존한 횟수
한 번도 GC 가 체크하지 않은 객체는 generation 0에 속함.
한 번 체크되었지만 생존한 객체는 generation 1에 속함.
두 번 이상 체크된 객체는 generation 2에 속함.

각 generation에 대한 threshold는 다음과 같음:
"""

DECRIPTION_2 = """
threshold0이 의미하는 것과 threshold1, threshold2가 의미하는 것은 다음과 같음:

threshold0:

(number of allocations) - (number of deallocations) > threshold0
위 조건을 만족하면 gen0 GC가 호출됨을 의미

기본 값은 700이며, (객체 생성수 - 객체 해제 수)가 700을 넘어가면 gen0 GC가 호출된다고 이해하면 됨

---

threshold1:

gen0 GC가 몇 번 호출되면 gen1 GC를 호출할 것인지 의미함

기본 값은 10이며, gen0 GC가 10번 호출되면 gen1 GC가 호출됨

threshold2:

마찬가지로 gen1 GC가 몇 번 호출되면 gen2 GC를 호출할 것인지 의미함

기본 값은 10이며, gen1 GC가 10번 호출되면 gen2 GC가 호출됨
다만 gen 2의 GC는 여기에 추가로

(long_lived_pending /long_lived_total)

위 조건이 25%를 넘을 경우에 수행됨
이러한 조건이 붙은 이유는 gen 2 GC를 수행하는데 오랜시간이 걸리기 때문

# https://devguide.python.org/internals/garbage-collector/index.html#collecting-the-oldest-generation
"""

print(DESCRIPTITON_1)
print(f"{gc.get_threshold() = }")
print()

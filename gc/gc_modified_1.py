import time
import gc

# pylint: disable=unused-import
# pylint: disable=unused-variable
# pylint: disable=disallowed-name

import numpy as np
import torch

# https://github.com/python/cpython/blob/46c808172fd3148e3397234b23674bf70734fb55/Modules/gcmodule.c#L417
gc.freeze()

class DummyClass:
    def __init__(self):
        self.foo = [[] for _ in range(4)]

def generate_objects() -> None:
    bar = [DummyClass() for _ in range(1000)]

times = []
for _ in range(500):
    start_time = time.time()
    generate_objects()
    times.append(time.time() - start_time)

avg_elapsed_time = sum(times) / len(times) * 1000
max_elapsed_time = max(times) * 1000

print(f"Average elapsed time: {avg_elapsed_time:.2f} ms")
print(f"Max elapsed time: {max_elapsed_time:.2f} ms")

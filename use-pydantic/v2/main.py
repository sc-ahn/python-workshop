import timeit
from random import random
from typing import List

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

def create_item() -> List[Item]:
    items = [
        Item(
            name=f"Item {i}",
            description=f"Description of item {i}",
            price=random() * 1000,
            tax=random(),
        ) for i in range(1000)
    ]
    return items

elapsed_time = timeit.timeit(create_item, number=1000)
print(f"Elapsed time: {elapsed_time * 1000:.2f}ms")

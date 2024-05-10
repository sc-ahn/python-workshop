import asyncio
from proc import afibo, measure_time

async def execute():
    tasks = [
        asyncio.create_task(afibo())
        for _ in range(10)
    ]
    for task in tasks:
        await task

@measure_time
def work():
    asyncio.run(execute())

if __name__ == '__main__':
    work()

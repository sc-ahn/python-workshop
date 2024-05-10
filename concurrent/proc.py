import inspect
from time import process_time_ns

async def afibo(n: int = 30):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return await afibo(n - 1) + await afibo(n - 2)

def fibo(n: int = 30):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

# decorator to measure time
def measure_time(func):
    def wrapper(*args, **kwargs):
        with open("measure_time.csv", "a", encoding="utf-8") as f:
            start = process_time_ns()
            result = func(*args, **kwargs)
            end = process_time_ns()
            f.write(
                f'{inspect.getfile(func).split("/")[-1].replace(".py", "")}'
                f',{end - start}\n'
            )
        return result
    return wrapper

from proc import fibo, measure_time

@measure_time
def work():
    for _ in range(10):
        fibo()

if __name__ == '__main__':
    work()

import multiprocessing
from proc import fibo, measure_time

@measure_time
def work():
    proc_list = []
    for _ in range(10):
        proc = multiprocessing.Process(target=fibo)
        proc.start()
        proc_list.append(proc)
    for p in proc_list:
        p.join()


if __name__ == '__main__':
    work()

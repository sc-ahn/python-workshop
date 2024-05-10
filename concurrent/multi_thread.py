import threading
from proc import fibo, measure_time

@measure_time
def work():
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibo)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()

if __name__ == '__main__':
    work()

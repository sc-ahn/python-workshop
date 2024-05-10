import threading
from inspect import getsource
from textwrap import dedent
import _xxsubinterpreters as interpreters
from proc import fibo, measure_time


def call_subinterpreter():
    process_str = dedent(getsource(fibo))
    intp_id = interpreters.create()
    interpreters.run_string(intp_id, process_str)
    interpreters.destroy(intp_id)

@measure_time
def work():
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=call_subinterpreter)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()

if __name__ == '__main__':
    work()

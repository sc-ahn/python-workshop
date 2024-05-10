import multiprocessing
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
    proc_list = []
    for _ in range(10):
        proc = multiprocessing.Process(target=call_subinterpreter)
        proc.start()
        proc_list.append(proc)
    for p in proc_list:
        p.join()

if __name__ == '__main__':
    work()

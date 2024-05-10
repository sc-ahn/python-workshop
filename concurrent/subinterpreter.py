from inspect import getsource
from textwrap import dedent
import _xxsubinterpreters as interpreters
from proc import fibo, measure_time

@measure_time
def work():
    process_str = dedent(getsource(fibo))
    for _ in range(10):
        intp_id = interpreters.create()
        interpreters.run_string(intp_id, process_str)
        interpreters.destroy(intp_id)

if __name__ == '__main__':
    work()

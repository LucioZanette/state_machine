import run_cython
import run_list
import time


def run():
    run_cython.run()


### --- run_list
start = time.time()
run_list.test()
end =  time.time()

py_time = end - start
print(f'run_list time = {py_time}')
print('-'*5)


### --- run_cython
start = time.time()
run_cython.run()
end =  time.time()

cy_time = end - start
print(f'run_cython time = {cy_time}')
print('-'*5)


print(f'Speedup = {py_time/cy_time}')
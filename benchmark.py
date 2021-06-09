import run
import run_switch
#import run_cython
import run_list
import time


start = time.time()
run.test()
end =  time.time()

py_time = end - start
print("run time = {}".format(py_time))

start = time.time()
run_list.test()
end =  time.time()

py_time = end - start
print("run_list time = {}".format(py_time))

start = time.time()
run_switch.test()
end =  time.time()

py_time = end - start
print("run_switch time = {}".format(py_time))

# start = time.time()
# run_cython.test()
# end =  time.time()

# cy_time = end - start
# print("run_cython time = {}".format(cy_time))

# print("Speedup = {}".format(py_time / cy_time))
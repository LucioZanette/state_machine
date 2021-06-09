#!/usr/bin/python3
# coding: utf-8

import os
import sys
import time
import logging
from cpython cimport array
from datetime import datetime


cdef init():
    print('run init')

    try:
        list_function = [
            function_5,
            function_1, 
            function_4, 
            function_2, 
            function_3, 
            final_function, 
        ]

        for func in list_function:
            func()
            
    except (Exception) as error:   
        print('Exception', error)


cdef void function_1():
    logging.debug('function 1 init')


cdef void function_2():
    logging.debug('function 2 init')
    #.set_state(FUNCTION_3)


cdef void function_3():
    logging.debug('function 3 init')


cdef void function_4():
    logging.debug('function 4 init')


cdef void function_5():
    logging.debug('function 5 init')


cdef void final_function():
    print('completed process')



cpdef void run():
    init()
    print('end')
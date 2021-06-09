#!/usr/bin/python3
# coding: utf-8

import os
import sys
import time
import logging
from cpython cimport array
from datetime import datetime

cdef int EXIT = 0  # exit must be zero
cdef int FUNCTION_1 = 1
cdef int FUNCTION_2 = 2
cdef int FUNCTION_3 = 3
cdef int FUNCTION_4 = 4
cdef int FUNCTION_5 = 5

cdef class StateMachine:

    cdef object __queue
    cdef int __run_machine

    def __cinit__(self):
        self.start_run()

    def __next__(self):
        try:
            # return the first state of the queue
            return self.__queue.pop(0)
        except:
            return 0

    cdef set_queue(self, queue):
        if queue is None:
            self.__queue = []
        else:
            self.__queue = list(queue)

    cdef start_run(self):
        self.__run_machine = 1

    cdef stop_run(self):
        self.__run_machine = 0

    cdef int must_run(self):
        return self.__run_machine

    cdef set_state(self, state):
        # insert state on the first position of the queue
        self.__queue.insert(0, state)

    cdef remove_state(self, state):
        self.__queue.remove(state)


cdef class TestClass(StateMachine):

    def __cinit__(self):
        cdef int[5] queue = [
            FUNCTION_5,
            FUNCTION_4, 
            FUNCTION_3, 
            FUNCTION_2, 
            FUNCTION_1, 
        ]
        self.set_queue(queue)

    def __del__(self):
        print('finish')

    def run(self):
        print('run init')

        self.start_run()

        try:
            while self.must_run():
                {
                    0: self.stop_run,
                    1: self.__function_1,
                    2: self.__function_2,
                    3: self.__function_3,
                    4: self.__function_4,
                    5: self.__function_5,
                }.get(next(self))()
                
        except Exception as error:
            logging.error(str(error))

    cdef void __function_1(self):
        logging.debug('function 1 init')

    cdef void __function_2(self):
        logging.debug('function 2 init')
        #self.set_state(FUNCTION_3)

    cdef void __function_3(self):
        logging.debug('function 3 init')

    cdef void __function_4(self):
        logging.debug('function 4 init')

    cdef void __function_5(self):
        logging.debug('function 5 init')


cpdef void test():
    cdef object test = TestClass()
    test.run()

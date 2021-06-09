#!/usr/bin/python3
# coding: utf-8

import os
import sys
import time
import logging
from datetime import datetime


class StopRun(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TestClass():

    def __init__(self):
        pass

    def __del__(self):
        print('finish')

    def stop_run(self):
        raise StopRun(message='completed process')

    def run(self):
        print('run init')

        try:
            list_function = [
                self.__function_1, 
                self.__function_2, 
                self.__function_3, 
                self.__function_4, 
                self.__function_5,
                self.stop_run, 
            ]

            for func in list_function:
                func()
                
        except (Exception, StopRun) as error:   
            if isinstance(error, StopRun):
                print('StopRun', error)
            else:
                print('Exception', error)

    def __function_1(self):
        logging.debug('function 1 init')

    def __function_2(self):
        logging.debug('function 2 init')
        #self.set_state(FUNCTION_3)

    def __function_3(self):
        logging.debug('function 3 init')

    def __function_4(self):
        logging.debug('function 4 init')

    def __function_5(self):
        logging.debug('function 5 init')


def time_it(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        end = time.time()
        print(f'Function took {end-start}s')

        return res

    return wrapper


@time_it
def run():
    test = TestClass()
    test.run()


def test():
    test = TestClass()
    test.run()

if __name__ == "__main__":
    run()

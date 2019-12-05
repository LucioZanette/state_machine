#!/usr/bin/python3
# coding: utf-8

import os
import sys
import time
import logging
from state_machine import StateMachine
from pyswitch import switch
from datetime import datetime

EXIT = 0  # exit must be zero
FUNCTION_1 = 1
FUNCTION_2 = 2
FUNCTION_3 = 3
FUNCTION_4 = 4
FUNCTION_5 = 5

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

log_name = '%s/log/test_%s.log' % (PROJECT_PATH,
                                   datetime.now().strftime('%Y%m%d'))

file_handler = logging.FileHandler(filename=log_name)
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
	level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
	handlers=handlers
)


class TestClass(StateMachine):

	def __init__(self):
		self.set_queue([
			FUNCTION_5,
			FUNCTION_4,
			FUNCTION_3,
			FUNCTION_2,
			FUNCTION_1,
		])

	def __del__(self):
		print('finish')

	def run(self):
		print('run init')

		self.start_run()

		try:
			while self.must_run():
				for case in switch(next(self)):
					if case(FUNCTION_1):
						self.__function_1()
						continue
					if case(FUNCTION_2):
						self.__function_2()
						continue
					if case(FUNCTION_3):
						self.__function_3()
						continue
					if case(FUNCTION_4):
						self.__function_4()
						continue
					if case(FUNCTION_5):
						self.__function_5()
						continue
					if case(EXIT):
						self.stop_run()
						break

		except Exception as error:
			logging.error(str(error))

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

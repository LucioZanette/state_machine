#!/usr/bin/python3
# coding: utf-8

import os
import logging
from state_machine import StateMachine
from datetime import datetime

EXIT = 0  # exit must be zero
FUNCTION_1 = 1
FUNCTION_2 = 2
FUNCTION_3 = 3
FUNCTION_4 = 4
FUNCTION_5 = 5

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

log_name = '%s/log/test_%s.log' % (PROJECT_PATH, datetime.now().strftime('%Y%m%d'))
logging.basicConfig(
	filename=log_name, 
	level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)


class TestClass(StateMachine):

	def __init__(self):
		self.set_queue([
			FUNCTION_3, 
			FUNCTION_1, 
			FUNCTION_5,
			FUNCTION_4, 
			FUNCTION_2, 
		])

		self.__switcher = {
			0: self.stop_run,
			1: self.__function_1,
			2: self.__function_2,
			3: self.__function_3,
			4: self.__function_4,
			5: self.__function_5,
		}


	def __del__(self):
		print('finish')

	def run(self):
		print('run init')

		self.start_run()

		try:
			while self.must_run():
				self.__switcher.get(next(self))()
				
		except Exception as error:
			logging.error(str(error))

	def __function_1(self):
		logging.debug('function 1 init')

	def __function_2(self):
		logging.debug('function 2 init')

	def __function_3(self):
		logging.debug('function 3 init')

	def __function_4(self):
		logging.debug('function 4 init')

	def __function_5(self):
		logging.debug('function 5 init')
		self.set_state(FUNCTION_3)


if __name__ == "__main__":

	test = TestClass()
	test.run()

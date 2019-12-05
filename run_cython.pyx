#!/usr/bin/python3
# coding: utf-8

import os
import sys
import time
import logging
from cpython cimport array
from state_machine import StateMachine
from datetime import datetime

cdef int EXIT = 0  # exit must be zero
cdef int FUNCTION_1 = 1
cdef int FUNCTION_2 = 2
cdef int FUNCTION_3 = 3
cdef int FUNCTION_4 = 4
cdef int FUNCTION_5 = 5

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

log_name = '%s/log/test_%s.log' % (PROJECT_PATH, datetime.now().strftime('%Y%m%d'))

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


cpdef void test():
	cdef object test = TestClass()
	test.run()
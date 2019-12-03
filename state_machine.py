# -*- coding: utf-8 -*-

class StateMachine:
	def __init__(self, queue=None):
		#print('StateMachine construct')
		self.set_queue(queue)
		self.start_run()

	def __next__(self):
		try:
			# return the first state of the queue
			return self.__queue.pop(0)
		except:
			return 0

	def set_queue(self, queue):
		if queue is None:
			self.__queue = []
		else:
			self.__queue = list(queue)

	def start_run(self):
		self.__run_machine = True

	def stop_run(self):
		self.__run_machine = False

	def must_run(self):
		return self.__run_machine

	def set_state(self, state):
		# insert state on the first position of the queue
		self.__queue.insert(0, state)

	def remove_state(self, state):
		self.__queue.remove(state)

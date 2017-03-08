'''
Created on Mar 5, 2017

@author: denis
'''

class Config(object):
	'''
	class to configure Aggregator
	(ojects that should be observed)
	'''
	def __init__(self):
		'''connection params'''
		self._host = 'localhost'
		self._port = 5672
		self._queue = 'sensor_queue'
		
		'''sensors and limits'''
		self._sensor_list = ['south_sensor', 'north_sensor',
                             'tmp_sensor']
		self._minSoC = 0.01
		self._maxSoC = 0.99
	
	
	@property
	def host(self):
		return self._host
	@property
	def port(self):
		return self._port
	@property
	def queue(self):
		return self._queue
	@property
	def sensor_list(self):
		return self._sensor_list
	@property
	def minSoC(self):
		return self._minSoC
	@property
	def maxSoC(self):
		return self._maxSoC




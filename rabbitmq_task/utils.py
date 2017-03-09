# -*- coding: utf-8 -*-

import time

def init_connection(connector, host, port):
	attempt = 0
	connection = None
	while not connection:
		try:
			connection = connector.BlockingConnection(connector.ConnectionParameters(host=host, port=port))
		except Exception as e:
			print 'Connection is unreachable because', e, attempt
			attempt += 1
			time.sleep(3)
			if attempt <= 5:
				continue
			else:
				raise Exception('Limit of attempts was reached')
		else:
			return connection

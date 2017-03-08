'''
Created on Mar 8, 2017

@author: denis
'''
import pika
import sys
import json
import optparse
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from config import Config


def main():
	parser = optparse.OptionParser("usage: %prog [options] arg1 arg2 arg3")
	parser.add_option("-S", "--stat_info", dest="stat_info",
						default="aggregation", type="string",
						help="specify sensor info point to observe")
	options, args = parser.parse_args()
	config = Config()
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=config.host, port=config.port))
	channel = connection.channel()
	properties = pika.BasicProperties(app_id='publisher',
	                                  content_type='application/json')
	message = json.dumps({'sensors':args})
	if args and set(args) <= set(config.sensor_list):
		exchange = 'units'
		channel.exchange_declare(exchange=exchange,
	                         type='direct')
		for el in args:
			channel.basic_publish(exchange='direct_logs',
			                      routing_key=el,
			                      body=message,
			                      properties=properties)
			print(" [x] Sent %r:%r" % (el, message))
	else:
		exchange = 'result'
		channel.exchange_declare(exchange=exchange,
	                         type='direct')
		channel.basic_publish(exchange=exchange,
	                          routing_key=exchange,
	                          body=message,
	                          properties=properties)
		print({'aggregated info': message})
	
	connection.close()


if __name__ == '__main__':
	main()
	
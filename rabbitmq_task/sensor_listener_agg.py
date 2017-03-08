'''
Created on Mar 8, 2017

@author: denis
'''
'''
Created on Mar 5, 2017

@author: denis
'''

import pika
import sys
import json
import random
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from config import Config


config = Config()

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=config.host, port=config.port))
channel = connection.channel()

channel.exchange_declare(exchange='result',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='result',
                   queue=queue_name,
                   routing_key='result')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
	active_sensor_list = list()
	inactive_sensor_list = list()
	common_SoC = 0
	average_SoC = 0
	remaining_capacity = 0
	number_of_units = 0
	number_of_active_units = 0
	units_out_of_boundaries = 0
	routing_key_list = config.sensor_list
	for routing_key in routing_key_list:
		active = random.choice([True, False])
		SoC = ("%.2f" % random.uniform(0, 1))
		total_capacity = ("%.2f" % random.uniform(1, 100))
		print SoC, active
		if active and float(SoC) >= config.minSoC and float(SoC)<=config.maxSoC:
# 		if active:
			print SoC, active
			active_sensor_list.append(routing_key)
			common_SoC += float(SoC)
			remaining_capacity += float(total_capacity) 
		else:
			inactive_sensor_list.append(routing_key)
	if common_SoC>0:
		average_SoC = common_SoC/len(active_sensor_list)
	number_of_active_units = len(active_sensor_list)
	number_of_units = len(active_sensor_list)+len(inactive_sensor_list)
	units_out_of_boundaries = len(inactive_sensor_list)
	
	result = ({'averageSoC':("%.2f" % average_SoC),
	       'remaining_capacity':("%.2f" % remaining_capacity),
	       'number_of_units':number_of_units,
	       'number_of_active_units':number_of_active_units,
	       'units_out_of_boundaries':units_out_of_boundaries})
	print result  

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

try:
	channel.start_consuming()
except KeyboardInterrupt:
	channel.stop_consuming()
finally:
	connection.close()


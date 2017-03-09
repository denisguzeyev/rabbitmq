# -*- coding: utf-8 -*-

'''
Created on Mar 8, 2017
@author: denis
'''

import random
import sys
from os import path

import pika


sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from config import Config
from utils import init_connection

config = Config()

connection = init_connection(connector=pika, host=config.host, port=config.port)

channel = connection.channel()

channel.exchange_declare(exchange='units',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

for severity in config.sensor_list:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    routing_key = method.routing_key
    active = random.choice([True, False])
    SoC = ("%.2f" % random.uniform(0, 1))
    total_capacity = ("%.2f" % random.uniform(1, 100))
    answer = {"routing_key": routing_key,
              'active': active,
              'SoC': SoC,
              'total_capacity': total_capacity}
    print answer


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
finally:
    connection.close()

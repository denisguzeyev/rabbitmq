Rabbit project
==============

Installation
------------
    ****Create virtualenv
    mkvirtualenv rabbit_project -p python
    or 
    virtualenv venv
    . venv/bin/activate
    
    ****If in development environment, install dev utils
    pip install -r requirements.txt
    
Running
------------
    
    ****For start containers run
    docker-compose up -d
    
    ****If you change code, get rid of containers
    docker rm -f $(docke ps -a)  
      
    and run next comand
    docker build .
    
    and then
    docker-compose up -d
    
In order to check sensors (with activated venv):
python rabbitmq_task/sensor_req.py south_sensor north_sensor tmp_sensor
Common aggregated info:
python rabbitmq_task/sensor_req.py


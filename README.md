Rabbit project
==============

Installation
------------
    ****Create virtualenv
    mkvirtualenv rabbit_project -p python
    
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
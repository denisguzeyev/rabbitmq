# Make a workdir and virtualenv
FROM ubuntu:latest

COPY . /app
WORKDIR /app

RUN apt-get update
RUN apt-get -y install python-pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["./rabbitmq_task/sensor_listener.py"]

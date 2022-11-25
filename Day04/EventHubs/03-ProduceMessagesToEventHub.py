#!/usr/bin/env python
#Create an event hub namespace 
#create an event hub veicleposition
#Create a SharedAccessPolicy copy connection string

# #Required for Event Hubs for kafka
from confluent_kafka import Producer,Consumer
import sys
import json
import datetime
import uuid
import random
conf = {
    'bootstrap.servers': 'carao2023eventhub.servicebus.windows.net:9093',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '$ConnectionString',
    'sasl.password': 'Endpoint=sb://carao2023eventhub.servicebus.windows.net/;SharedAccessKeyName=readwrite;SharedAccessKey=eOlZaWO4qP/etM4GPkOcw98vbZXb6JLXPmUrpBJdSOQ=',
    'client.id': 'socket.gethostname()'
}
# Create Producer instance
p = Producer(**conf)

def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        print('Message delivered to {} {} @{} {} \n'.format(msg.topic(), msg.partition(), msg.offset(),msg.value()))

#  topic name which is the event hub name
topic= 'vehicleposition'
devices = []
for x in range(0, 10):  
    devices.append(str(uuid.uuid4()))
for y in range(0,20):    # For each device, produce 20 events. 
    for dev in devices:
        try:
        # Create a dummy vehicle reading.
            reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
            msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
            p.produce(topic, msgformatted, callback=delivery_callback)
            p.flush()
        except BufferError as e:
            sys.stderr.write('some error')
sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
p.flush()
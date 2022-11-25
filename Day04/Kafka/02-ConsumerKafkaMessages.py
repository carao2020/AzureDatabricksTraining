from kafka import KafkaConsumer


consumer=KafkaConsumer(bootstrap_servers=['20.119.101.82:9092'], auto_offset_reset='earliest',api_version=(0, 10, 1))
consumer.subscribe(['VehicleDetails'])
for msg in consumer:
    print (msg)

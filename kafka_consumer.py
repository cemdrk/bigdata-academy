from kafka import KafkaConsumer

consumer = KafkaConsumer('user', bootstrap_servers=['localhost:9092'])

for msg in consumer:
    print(msg.value.decode('utf-8'))

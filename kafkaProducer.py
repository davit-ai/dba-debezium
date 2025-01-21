from kafka import KafkaProducer

bootstrap_servers = 'localhost:29092'
topicName = 'school'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer.send(topicName, value=b'Hello, lol!')
producer.flush()  # Ensure all messages are sent before exiting
print('Message sent to Kafka topic:', topicName)
from kafka import KafkaConsumer

bootstrap_servers = 'localhost:29092'
topicName = 'test'
consumer = KafkaConsumer(topicName,auto_offset_reset='earliest', bootstrap_servers=bootstrap_servers)
for msg in consumer:
    print("Topic Name=%s, Message=%s" % (msg.topic, msg.value))

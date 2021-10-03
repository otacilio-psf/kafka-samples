from confluent_kafka import Producer
import json

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

data_source = [
    {"key": "msg_1", "value": { "id": "5001", "type": "None" }},
    {"key": "msg_2", "value": { "id": "5002", "type": "Glazed" }},
    {"key": "msg_3", "value": { "id": "5005", "type": "Sugar" }},
    {"key": "msg_4", "value": { "id": "5003", "type": "Chocolate" }},
    {"key": "msg_5", "value": { "id": "5004", "type": "Maple" }}
]

for data in data_source:
    p.poll(0)
    p.produce('cake-topping', key=data["key"], value=json.dumps(data["value"]).encode('utf-8'), callback=delivery_report)

p.flush()

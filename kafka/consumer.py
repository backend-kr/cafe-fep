# cafe_info_kafka_consumer_example.py
from confluent_kafka import Consumer, KafkaError
import json

conf_consumer = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'cafe_info_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf_consumer)
topic = 'cafe-info'

def process_cafe_info(msg_value):
    cafe_info = json.loads(msg_value)
    print("Received cafe info:")
    for key, value in cafe_info.items():
        print(f"{key}: {value}")

def is_specific_neighborhood_cafe(cafe_info, neighborhood_name):
    return neighborhood_name in cafe_info['address']

def consume_cafe_info(topic, neighborhood_name):
    consumer.subscribe([topic])
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
            else:
                cafe_info = json.loads(msg.value())
                if is_specific_neighborhood_cafe(cafe_info, neighborhood_name):
                    process_cafe_info(msg.value())
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    neighborhood_name = '합정동'
    consume_cafe_info(topic, neighborhood_name)

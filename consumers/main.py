from pykafka import KafkaClient


def main():
    client = KafkaClient(hosts="localhost:39092")
    topic = client.topics[b'my.test']

    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)


if __name__ == '__main__':
    main()

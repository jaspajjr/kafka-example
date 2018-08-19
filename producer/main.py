from pykafka import KafkaClient


def main():
    client = KafkaClient(hosts="localhost:39092")
    topic = client.topics[b'my.test']

    with topic.get_sync_producer() as producer:
        for i in range(4):
            msg = 'test message: {0} '.format(i ** 2)
            producer.produce(msg.encode('utf-8'))


if __name__ == '__main__':
    main()

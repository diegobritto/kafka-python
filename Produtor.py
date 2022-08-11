from kafka import KafkaProducer as kp
import random
produtor = kp(bootstrap_servers="127.0.0.1:9092")
for x in range(10):
    n = random.random()
    produtor.send("mensagens", key=b"Chave %d" % x, value=b"Mensagem %f " % n)
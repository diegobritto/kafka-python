
# 
# Instalação e Primeiros Passos
1. atualizar pacotes de sistema 
 
```
sudo apt update
sudo apt -y upgrade
```
2.  instalar Java

```
sudo apt install curl mlocate default-jdk -y
```

3. #verificar versão
```
java -version
```
4. descompactar
```
tar -xzf kafka_2.13-2.8.0.tgz
```
5. iniciar zookeeper
```
./zookeeper-server-start.sh ../config/zookeeper.properties
```
6. iniciar broker
```
./kafka-server-start.sh ../config/server.properties
```
7. criar topico
```
./bin/kafka-topics.sh --create --topic ola-mundo --bootstrap-server localhost:9092
```
8. enviar mensagem producer
```
./kafka-console-producer.sh --topic ola-mundo --bootstrap-server localhost:9092
```
9. consumir
```
bin/kafka-console-consumer.sh --topic ola-mundo --from-beginning --bootstrap-server localhost:9092
```
10. listar
```
./kafka-topics.sh --zookeeper localhost:2181 --list
```
12. descrever
```
./kafka-topics.sh --describe --topic ola-mundo --bootstrap-server localhost:9092
```
# 
# Utilizando Kafka

## Topics
1. lista os topicos existentes
```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list 
```

2. criamos um novo tópico com 3 particoes e 1 fator de replicação
```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic novotopico --create --partitions 3 --replication-factor 1
```

3. lista os topicos existentes

```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list 
```

4. descreve

```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic novotopico --describe
```

5. alterar partições

```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic novotopico --alter --partitions 4
```


6. exclusão

```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic novotopico --delete
```



## Producer
1. criamos tópico
```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --create --partitions 3 --replication-factor 1
```

2. console producer
```
./kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092  --topic mensagens
```

3.  enviar mensagem para topico não existente
```
./kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092  --topic novasmensagens
```

4. listamos os topicos para confirmar a criação
```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list 
```

## Consumer

1. Consumir do inicio
```
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --from-beginning
```
2. Producer
```
./kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092  --topic mensagens
```
3. consumir com off set
```
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 0 --offset 2
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 1 --offset 2
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 2 --offset 2
```
4. max messagens 
```
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 2 --offset 2 --max-messagens 1
```
5. consumir de partições
```
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 0
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 1
./kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partions 2
```

## Groups

1. Cria um consumidor com um grupo
```
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```
2. Cria outro consumidor com o mesmo grupo
```
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```
3. Cria um consumidor do mesmo topico mas de outro grupo
```
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group novosconsumidores
```
4. mostra consumers groups
```
./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```
5. descrever grupos
```
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group consumidores
```
6. abrir um novo consumidor usando from beggining
```
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores --from-beginning
```
7. reset do offset
```
./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group consumidores --topic mensagens --reset-offsets --to-earliest --execute 
```
8. novo consumidor para o grupo, as mensagens devem ser lidas desde o inicio
```
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```


# Criando um cluster
## Criando
1. parar kafka e zookeeper
```
./kafka-server-stop.sh
./zookeeper-server-stop.sh
```
2. apagar o diretorio de topicos
```
rm -r kafka*
rm -r zookeeper
```
3. copiamos o arquivo de configuração do server
```
cp server.properties server.properties0
cp server.properties server.properties1
cp server.properties server.properties2
```
4. inicia zookeeper
```
./zookeeper-server-start.sh ../config/zookeeper.properties
```
5. inicia brokers
```
./kafka-server-start.sh ../config/server.properties0
./kafka-server-start.sh ../config/server.properties1
./kafka-server-start.sh ../config/server.properties2
```
6. checar
```
./zookeeper-shell.sh localhost:2181 
ls /brokers/ids
get /brokers/ids/1
```
## Usando

1. criamos um novo tópico com 3 particoes e 3 fator de replicação
```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --create --partitions 3 --replication-factor 3
```
2. descreve
```
./kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --topic novotopico --describe
```
3. console producer
```
./kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092  --topic mensagens
```
4. Cria um consumidor com um grupo
```
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```
5. descrever grupos
```
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group consumidores
```
6. mostrar dados
```
cd /tmp/kafka-logs/
```
7. ler os dados
```
Kafka-dump-log.sh
```

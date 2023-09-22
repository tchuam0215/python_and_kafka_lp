# python-and-kafka-lp-author
**Repository for liveProject: Python and Kafka**


## 1st Delivery 

* Create the sample_project python project
* Create a virtual environment 
* Install poetry 
* Add the "requests" python package
* scrap manning.com website to get the html code 

## 2nd Delivery 

### Start testing and interacting with Kafka running in the Docker container on your computer

**1. You need to launch the containers using docker-compose :**

```docker
$ docker-compose --file docker-compose.yml up --detach
```

**2. Open 02 CLI :**

>Run the following command in the first CLI to send messages
```docker 
docker-compose exec -it kafka kafka-console-consumer.sh --consumer.config /opt/bitnami/kafka/config/consumer.properties --bootstrap-server kafka:9092 --topic test --from-beginning
```
>Then run the following command in the second CLI to receive messages  
```docker 
docker-compose exec -it kafka kafka-console-producer.sh --producer.config /opt/bitnami/kafka/config/producer.properties --bootstrap-server 127.0.0.1:9094 --topic test
```
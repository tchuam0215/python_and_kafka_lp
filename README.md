# python-and-kafka-lp-author
**Repository for liveProject: Python and Kafka**


## 1st Delivery 

## Using python for the first time

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

## 3rd Delivery 

### Working with a Postgres Database

The deliverable for this milestone is a docker-compose file consisting of three running containers: Kafka, Zookeeper, and Postgres
When running :
```docker
docker-compose --file ./docker-compose.yml up --detach 
```
The service postgresql automaticaly restore the pagila database, you can then verify this database with the following commands :

1. Log in to the postgresql database service   : 
```docker
docker-compose exec -it postgresql psql -U postgres
```
2. List the database :
```sql
postgres>\l
```
3. Connect to the database **pagila**
```sql
postgres>\connect pagila
```
4. You are free to run some queries : 
```sql
postgres>select * from actor limit 10;
```

# Observability project

Objective

* Kick off Kafka to start the data pipeline; in other words, what we did at the end of Project 1, Milestone 3.

* Remember, we can do this through the console using the docker-compose command.
Create a Python program utilizing the Faust library to communicate with Kafka, proving the ability to produce and consume messages.

NB : i have installed python 3.9.18, this version well form me with faust library without any dependency issues. 

1. First you need a hello_world.py, you can find this [Quickstart from faust official library](https://faust.readthedocs.io/en/latest/playbooks/quickstart.html#quickstart) :
```python
import faust

app = faust.App(
    'hello-world',
    broker='kafka://localhost:9094',  # Point to the Kafka broker
    value_serializer='raw',           # Use raw (unencoded) message format
)

greetings_topic = app.topic('greetings')

@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(f"Received: {greeting.decode('utf-8')}")

if __name__ == '__main__':
    app.main()
```

_NB : this code is enough to start._  

2. Start Kafka using the you docker compose file (follow the step above)

3. Run the faust worker : 

Now that you have created a simple Faust application and have Kafka and Zookeeper running, you need to run a worker instance for the application.

Multiple instances of a Faust worker can be started independently to distribute stream processing across machines and CPU cores.

Start the worker :
```bash
poetry run faust -A hello_world worker -l info
```
Now that you worker is running, open a new terminal where you are going to produce messages, we are going to use 02 methods to send messages : 
```bash
# this is a one shot producer
poetry run faust -A hello_world send @greet "Hello Faust"
```
or

```bash 
# this is a one shot producer 
poetry run faust -A hello_world send greetings "Hello Kafka topic"
```
or

```bash
# you can send message continuously 
docker-compose exec -it kafka kafka-console-producer.sh --producer.config /opt/bitnami/kafka/config/producer.properties --bootstrap-server 127.0.0.1:9094 --topic greetings
```

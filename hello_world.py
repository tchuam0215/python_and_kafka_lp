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

from fastapi import Body, FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from kafka_producer import AIOProducer
from confluent_kafka import avro
from models import *
from pydantic import BaseModel, ValidationError, validator

app = FastAPI()

booking_schema = avro.load('schemas/booking-schema.avsc')
booking_producer = None
booking_topic = 'booking-topic'

event_schema = avro.load('schemas/event-schema.avsc')
event_producer = None
event_topic = 'event-topic'

local_config = {'bootstrap.servers': 'localhost:9092', 'schema.registry.url': 'http://127.0.0.1:8081'}

@app.on_event("startup")
async def startup_event():
    global booking_producer
    booking_producer = AIOProducer(local_config,  default_value_schema=booking_schema)
    global event_producer
    event_producer = AIOProducer(local_config,  default_value_schema=event_schema)

@app.on_event("shutdown")
def shutdown_event():
    booking_producer.close()
    event_producer.close()

@app.post("/inbound-bookings")
async def bookings(data: Ably_webhook, request: Request):

    booking_records = []
    try:
        booking_records = [booking_producer.produce(booking_topic, Booking.parse_raw(x.data)) for x in data.items[0].data.messages]
        
    except ValidationError as e:
        print(e)
        return 400
    return 200


@app.post("/inbound-events")
async def event_creation(data: Event, request: Request):

    try:
        event_producer.produce(event_topic, data)
    except ValidationError as e:
        print(e)
        return 400
    
    return 200


@app.post("/presence")
async def presence_firehose(data: Ably_webhook, request: Request):
    # print(data)
    # all presence events
 
    return 200



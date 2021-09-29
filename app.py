
from fastapi import Body, FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from kafka_producer import AIOProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka import SerializingProducer
from pathlib import Path 
from models import *
from pydantic import BaseModel, ValidationError, validator

app = FastAPI()

booking_schema = Path('schemas/booking-schema.avsc').read_text()
booking_producer = None
booking_topic = 'booking-topic'

event_schema = Path('schemas/event-schema.avsc').read_text()
event_producer = None
event_topic = 'event-topic'

local_config = {'bootstrap.servers': 'localhost:9092'}
schema_registry_local = {'url': 'http://127.0.0.1:8081'}

schema_registry_client = SchemaRegistryClient(schema_registry_local)
booking_avro_serializer = AvroSerializer(schema_registry_client = schema_registry_client,
                                          schema_str = booking_schema)
event_avro_serializer = AvroSerializer(schema_registry_client = schema_registry_client,
                                          schema_str = event_schema)
                                          
event_config = {'bootstrap.servers': 'localhost:9092', 'value.serializer': event_avro_serializer}
booking_config = {'bootstrap.servers': 'localhost:9092', 'value.serializer': booking_avro_serializer}
@app.on_event("startup")
async def startup_event():
    global booking_producer
    booking_producer = SerializingProducer(booking_config)
    global event_producer
    event_producer = SerializingProducer(event_config)

@app.on_event("shutdown")
def shutdown_event():
    booking_producer.close()
    event_producer.close()

@app.post("/inbound-bookings")
async def bookings(data: Ably_webhook, request: Request):
    try:
        booking_list = [Booking.parse_raw(x.data) for x in data.items[0].data.messages]
        for booking_entry in booking_list:
            booking_producer.produce(booking_topic, None, booking_entry.dict())
    except Exception as e:
        print(e)
        return 400
    return 200


@app.post("/inbound-events")
async def event_creation(data: Event, request: Request):
    try:
        event_producer.produce(event_topic, None, data.dict())
        event_producer.poll(0)
        event_producer.flush()
    except Exception as e:
        print(e)
        return 400
    
    return 200

@app.post("/presence")
async def presence_firehose(data: Ably_webhook, request: Request):
    # print(data)
    # all presence events
 
    return 200



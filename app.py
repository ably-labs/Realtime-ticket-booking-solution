
from fastapi import Body, FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles 
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

conference_schema = Path('schemas/conference-schema.avsc').read_text()

conference_producer = None
conference_topic = 'conference-topic'

local_config = {'bootstrap.servers': 'localhost:9092'}
schema_registry_local = {'url': 'http://127.0.0.1:8081'} 

booking_avro_serializer = AvroSerializer(schema_registry_client = SchemaRegistryClient(schema_registry_local), schema_str = booking_schema)
conference_avro_serializer   = AvroSerializer(schema_registry_client = SchemaRegistryClient(schema_registry_local), schema_str = conference_schema)
                                          
conference_config   = {'bootstrap.servers': 'localhost:9092', 'value.serializer': conference_avro_serializer}
booking_config = {'bootstrap.servers': 'localhost:9092', 'value.serializer': booking_avro_serializer}

@app.on_event('startup')
async def startup_event():
    global booking_producer
    booking_producer = SerializingProducer(booking_config)
    global conference_producer
    conference_producer = SerializingProducer(conference_config)

@app.on_event('shutdown')
def shutdown_event():
    booking_producer.close()
    conference_producer.close()

@app.post('/inbound-bookings')
async def bookings(data: Ably_webhook, request: Request):
    try:
        booking_list = [Booking.parse_raw(x.data) for x in data.items[0].data.messages]
        for booking_entry in booking_list:
            booking_producer.produce(booking_topic, None, booking_entry.dict())
        booking_producer.poll(0)
        booking_producer.flush
    except Exception as e:
        print(e)
        return 400
    return 200

@app.post('/inbound-conferences')
async def conference_creation(data: Conference, request: Request):
    try:
        conference_producer.produce(conference_topic, None, data.dict())
        conference_producer.poll(0)
        conference_producer.flush()
        print (data.dict())
    except Exception as e:
        print(e)
        return 400
    
    return 200

@app.post('/presence')
async def presence_firehose(data: Ably_webhook, request: Request):
    # print(data)
    # all presence events
 
    return 200



import asyncio
from ably import AblyRest
import datetime
import json
import names
import random


# this should be the name of an event in your current events stream
# I have chosen one from at random
event_name = "William's big event"

# A sample booking JSON that matches the schema in the models expected by system
mybooking  =  {
    "userId": "",
    "eventId": event_name,
    "ticketNumber": 1,
    "timestamp": 0
}

# as we are only hitting one event we should not book too many tickets at once
number_of_bookings = 5


# simple Ably publisher from https://github.com/ably/ably-python
# please add your API here
ably = AblyRest('APIKEY')
channel = ably.channels.get("bookings:booking1")
for count in range(number_of_bookings):
    mybooking["userId"] = names.get_full_name()
    mybooking["ticketNumber"] = random.randint(1,5)
    mybooking["timestamp"] = int((datetime.datetime.now() - datetime.timedelta(days=random.randint(1,10))).timestamp()) 
    channel.publish('booking', mybooking)


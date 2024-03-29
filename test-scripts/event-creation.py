import datetime
import json
import names
import random
import requests

# This is the layout of the event creation message as seen in the open API spec when you start the main API
my_event = {
    "eventId": "string",  # A string to identify the event, would likely be a UUID and a display name in a
                          # more complete implementation

    "eventCapacity": 0,   # The max number of people allowed at the event, in later examples we could have
                          # a structure for different seating types

    "eventDate": 0,       # Event date as a UTC timestamp
    "bookingStart": 0,    # Booking window start as a UTC timestamp
    "bookingEnd": 0,      # Booking window end as a UTC timestamp
    "timestamp": 0        # Event creation timestamp unused at the moment UTC timestamp
    }

target_url = 'http://127.0.0.1:8000/inbound-conferences'  # url for the event creation endpoint set for local dev.

events = 20  # number of events to make

first_event = datetime.datetime.now()  # this today,  we are going to create events offset from this

time_delta = datetime.timedelta(days=7)  # days between each event, a week in this case

booking_window = datetime.timedelta(days=30)  # base days of the booking window

current_date = first_event  # and then we have the moving 

#  we are going to create a stream events to match against
for count in range(events):
    current_date = current_date + time_delta
    date_offset = current_date - datetime.timedelta(days=1)
    my_event["eventId"] = names.get_first_name() + "'s big event"
    my_event["eventCapacity"] = random.randint(50, 400)
    my_event["eventDate"] = int(current_date.timestamp())
    my_event["bookingEnd"] = int(date_offset.timestamp())  # booking ends a day before
    my_event["bookingStart"] = int((date_offset - booking_window).timestamp())  # booking starts 30 days before
    r = requests.post(target_url, data=json.dumps(my_event))
    print(json.dumps(my_event))











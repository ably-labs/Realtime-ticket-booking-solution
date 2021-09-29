import json
import names
import random
import requests
import datetime


#This is the layout of the event creation message as seen in the open API spec when you start the main API
my_event =  {
    "eventId": "string",  #A string to idenfity the event, would likely be a UUID and a display name in a more complete implimentation
    "eventCapacity": 0,   #The max number of people allowed at the event, in later examples we could have a structure for different seating types
    "eventDate": 0,       #Event date as a UTC timestamp
    "bookingStart": 0,    #Booking window start as a UTC timestamp
    "bookingEnd": 0,      #Booking window end as a UTC timestamp
    "timestamp": 0        #Event creation timestamp unused at the moment UTC timestamp
    }


events = 20 # number of events to make

first_event = datetime.datetime.now()	# this today,  we are going to create events offset from this

time_delta = datetime.timedelta(days=7) # days between each event, a week in this case

booking_window = datetime.timedelta(days=30) # base days of the booking window

current_date = first_event  # and then we have the moving 

#we are going to create a stream events to match against
for count in range(events):
    current_date = current_date + time_delta
    my_event["eventId"] = names.get_first_name() + "s big event"
    my_event["eventCapacity"] = random.randint(50, 400)
    my_event["eventDate"] = int(current_date.timestamp())
    my_event["bookingEnd"] = int((current_date - datetime.timedelta(days=1)).timestamp()) #booking ends a day before
    my_event["bookingStart"] = int(((current_date - datetime.timedelta(days=1)) - booking_window).timestamp())  # booking starts 30 days before
    r = requests.post('http://127.0.0.1:8000/inbound-events', data = json.dumps(my_event))
    print(json.dumps(my_event))











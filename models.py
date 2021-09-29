from pydantic import BaseModel
from typing import *
from datetime import date, datetime, time, timedelta


class Event(BaseModel):
    eventId: str
    eventCapacity: int
    eventDate: int
    bookingStart: int
    bookingEnd: int
    timestamp: int
    pass

class Booking(BaseModel):
    userId: str
    eventId: str
    ticketNumber: int
    timestamp: datetime
    pass

class Cancellation(BaseModel):
    userId: str
    eventId: str
    ticketNumber: int
    timestamp: datetime
    pass

class Presence_message(BaseModel):
    id: str
    clientId: str
    connectionId: str
    timestamp: datetime
    data: Optional[Union[dict, str]]
    action: int
    pass


class Presence_wrapper(BaseModel):
    channelId: str
    site: str
    presence: List[Presence_message]
    pass

class Ably_webhook_message(BaseModel):
    id: str
    timestamp: datetime
    data: str # Ably stringifies the data here
    name: str
    pass

class Webhook_data(BaseModel):
    channelId: str
    site: str
    messages: List[Ably_webhook_message]
    pass

class Webhook_item(BaseModel):
    webhookId: str
    source: str
    timestamp: datetime
    serial: Optional[str] = None
    name: str
    data: Union[Webhook_data, Presence_wrapper]
    pass

class Ably_webhook(BaseModel):
    items: List[Webhook_item]
    pass


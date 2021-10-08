from pydantic import BaseModel
from typing import *
from datetime import datetime


class Conference(BaseModel):
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
    timestamp: int
    pass


class Cancellation(BaseModel):
    userId: str
    eventId: str
    ticketNumber: int
    timestamp: datetime
    pass


class PresenceMessage(BaseModel):
    id: str
    clientId: str
    connectionId: str
    timestamp: datetime
    data: Optional[Union[dict, str]]
    action: int
    pass


class PresenceWrapper(BaseModel):
    channelId: str
    site: str
    presence: List[PresenceMessage]
    pass


class AblyWebhookMessage(BaseModel):
    id: str
    timestamp: datetime
    data: str  # Ably stringifies the data here
    name: str
    pass


class WebhookData(BaseModel):
    channelId: str
    site: str
    messages: List[AblyWebhookMessage]
    pass


class WebhookItem(BaseModel):
    webhookId: str
    source: str
    timestamp: datetime
    serial: Optional[str] = None
    name: str
    data: Union[WebhookData, PresenceWrapper]
    pass


class AblyWebhook(BaseModel):
    items: List[WebhookItem]
    pass


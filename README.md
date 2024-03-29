# Realtime ticket booking solution


Welcome to the Ably Realtime ticket booking solution!
This demo expects you to have a version of the [Confluent Platform](https://docs.confluent.io/platform/current/quickstart/ce-quickstart.html) up and running with Kafka, ksqlDB, and Schema Registry. The defaults in the code are for the stand alone broker, although these can be replaced with cloud config or a local Docker config. 
In addition, we will use several other technologies to build the ticket booking solution:
* [ably](https://ably.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Ngrok](https://ngrok.com/)

For detailed instructions, [please refer to the technical guide](https://ably.com/blog/realtime-ticket-booking-solution-kafka-fastapi-ably). 

Useful Resources:

* [Ably Kafka Connector: extend Kafka to the edge reliably and safely](https://ably.com/blog/ably-kafka-connector-extend-kafka-to-the-edge)
* [Building a realtime ticket booking solution with Kafka, FastAPI, and Ably](https://ably.com/blog/realtime-ticket-booking-solution-kafka-fastapi-ably#building-the-realtime-ticket-booking-solution)
* [How to stream Kafka messages to Internet-facing clients over WebSockets](https://ably.com/topic/websockets-kafka)



CREATE STREAM conferences WITH(
    KAFKA_TOPIC = 'conference-topic',
    VALUE_FORMAT = 'AVRO'
)

CREATE STREAM current_conferences AS SELECT * FROM conferences
 WHERE BOOKINGSTART < (UNIX_TIMESTAMP()/1000)
 AND BOOKINGEND > (UNIX_TIMESTAMP()/1000)
EMIT CHANGES;

CREATE TABLE booking_list(
     id bigint PRIMARY KEY
   ) WITH (
     KAFKA_TOPIC = 'booking-topic', 
     VALUE_FORMAT = 'AVRO'
   );

CREATE TABLE bookings_per_event AS
  SELECT eventID,
        SUM(TICKETNUMBER) AS TOTAL_BOOKINGS
  FROM  BOOKINGS 
  GROUP BY eventID;

CREATE STREAM output_stream
    WITH (kafka_topic='out-topic',
          value_format='json') AS
    SELECT current_conferences.EVENTID as id, EVENTCAPACITY, TOTAL_BOOKINGS, EVENTDATE, BOOKINGSTART, BOOKINGEND 
    FROM current_conferences
    LEFT JOIN BOOKINGS_PER_EVENT ON  current_conferences.EVENTID = BOOKINGS_PER_EVENT.EVENTID;

--  this are some experimental queries that make some interesting tables which are worth exploring
CREATE TABLE conference_list(
     id bigint PRIMARY KEY
   ) WITH (
     KAFKA_TOPIC = 'conference-topic', 
     VALUE_FORMAT = 'AVRO'
   );

CREATE TABLE current_conference_list AS SELECT * FROM conference_list
 WHERE BOOKINGSTART < (UNIX_TIMESTAMP()/1000)
 AND BOOKINGEND > (UNIX_TIMESTAMP()/1000)
 EMIT CHANGES;
These are the topic schemas for the main inbound topics.
Having them set up as Avero in schema registry makes it easier to use them with KSQLDB

The outbound topic is derived from the SQL commands we will be running as will ne JSON hence is untyped.

The serialising producers read these and add will them the schema registry on start so there is no need to configure them manually.
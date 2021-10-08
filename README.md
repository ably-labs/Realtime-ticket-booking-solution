# booking-calander

Welcome to The Ably Booking Calander API Demo.  

This demo expects you to have a version of the (Confluent Platform)[https://docs.confluent.io/platform/current/quickstart/ce-quickstart.html] up and running with ksqlDB + schema registry. The defaults in the code are for the stand alone broker though these can be replace with cloud config or a local docker config.
For more detaield instructions please see (the blog)[wwww.ably.com]

To start the application: use the following: 

uvicorn app:app --reload


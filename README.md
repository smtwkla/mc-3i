# 3i
## IoT device - [ MQTT ] -> MQTT Broker ->  MySQL database -> Device Logic Code

3i is a python based MQTT Client that saves MQTT messages to MySQL database. Rules can be configured to save messages that match a topic to a MySQL table. Data has to arrive on the MQTT messages as a JSON text string with the following format:

{ "field1" : "val1", "field2" : 0, "field3" : "1/1/1" }

## Requirements:

*   paho - Python MQTT Client library
*   PyMySQL - Python MySQL Client library

## MQTT Message Listener Processing Rules

Rule Name, MQTT Topic to subscribe, MySQL table name to Save data, Operation: INSERT / UPDATE, key field for update

## Configuration:

All config information is stored in .json files in JSON format.

### MQTT Server Config:

Settings saved in mqtt_config.json file are : MQTT Host Name, Port, Username, Password

### Database Server Config:

db_config.json conntains the following settings for the MySQL server to connect to: Host, Port, Username, password, DB name

### Rule Config:

topic_config.json file contains rule definitions. Example config below:

    {
      "TOPIC1": {
        "TOPIC" : "testTopic/#",
        "TABLE" : "test1",
        "INSERT" : 1
      },
      "TOPIC2": {
        "TOPIC" : "testTopic2",
        "TABLE" : "test2",
        "INSERT" : 1
      },
      "TOPIC3": {
        "TOPIC" : "testTopic3",
        "TABLE" : "test3",
        "INSERT" : 1
      }
    }

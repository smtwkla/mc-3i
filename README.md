# 3i
## IoT device - [ MQTT ] <-> MQTT Broker <-> 3i platform <-> Device Logic Code <-> MySQL database 

3i is a python based IOT Platform with MQTT Client. It contains a ThingsRegistry, Rules Manager, Action, Database interface (MySQL), custom ThingsClasses for business logic.

## Requirements:

*   paho - Python MQTT Client library
*   PyMySQL - Python MySQL Client library

## Configuration:

All config information is stored in .json files in JSON format in the conf folder. Rename the .json.sample files as .json files and make changes as necessary.

### MQTT Server Config:

Settings saved in mqtt_config.json file are : MQTT Host Name, Port, Username, Password
This file also contains the site wide IOT MQTT Prefix.

### Database Server Config:

db_config.json conntains the following settings for the MySQL server to connect to: Host, Port, Username, password, DB name

### Rule Config:

## MQTT Message to Direct Database Table Rules:

topic_config.json file contains rule definitions. 

Rule Name, MQTT Topic to subscribe, MySQL table name to Save data, Operation: INSERT / UPDATE, key field for update [update not yet supported]

Example config below:

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

Data has to arrive on the MQTT messages as a JSON text string with the following format:

{ "field1" : "val1", "field2" : 0, "field3" : "1/1/1" }

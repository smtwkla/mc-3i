# 3i
 
3i is a python based IOT Platform. It contains of modules iot-3i, mc-3i, daq-3i and web-3i.

mc-3i is a machine model controller for digital replica management. It gets data from sources and upates the digital model. It has a ThingsRegistry, Rules Action, Database interface (MySQL) and MQTT Client. It supports custom ThingsClasses for business logic.

    IoT device <-> MQTT Broker <-> mc-3i platform <-> Device Logic Code <-> MySQL database

## Requirements:

*   paho - Python MQTT Client library
*   PyMySQL - Python MySQL Client library

## Command line parameters Syntax:

    python 3i   [ -d Folder_Containing_db_config.json ] 
                [ -c Folder_Containing_JSON_Config_files ]
                [ MODE_ACTION ]
                [ -L DEBUG ]
                [ -LF logfile_path ]
    
## Configuration:

All config information is stored in .json files in JSON format in the conf folder. If path for config files is not specified, 3i looks for all config files in conf/ subdirectory. Rename the .json.sample files as .json files and make changes as necessary.

### MQTT Server Config:

Settings saved in mqtt_config.json file are : MQTT Host Name, Port, Username, Password
This file also contains the site wide IOT MQTT Prefix.

### Database Server Config:

db_config.json contains the following settings for the MySQL server to connect to: Host, Port, Username, password, DB name

# Starting Modes

3i can be started in two modes : Things mode and Rules mode. In Things mode, 3i loads ThingsRegistry and Things objects. Things subscribe to MQTT topics and they are processed. In Rules mode, 3i processes the Rule Action table.

### Things Mode:

Things configured in things_config.json are loaded by the Things Register. Sample configuration:

    {
      "PK1": {
        "TID" : "PK1",
        "CLASS" : "APK_ThingClass",
        "DESC" : "Automatic Packing Machine 1"
      },
    
      "PK2": {
        "TID" : "SAPK2",
        "CLASS" : "APK_ThingClass",
        "DESC" : "Semi-Automatic Packing Machine 2"
      },
    
      "WT1": {
        "TID": "WT1",
        "CLASS" : "ThingClass",
        "DESC" : "Water Tank 1"
      }
    }
### Action Rule Mode:
 To start 3i in Action rule processing mode, use:
    
    python 3i MODE_ACTION
     
### MQTT to Direct Database Table - Configuration Rules:

direct2db_config.json file contains rule definitions. 

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

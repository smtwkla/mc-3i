
import mqtt_config

conf=mqtt_config.read_mqtt_conf()

print "config:"
print conf['mqtt_host'] + " " + str(conf['mqtt_port']) + " " +  conf['mqtt_username'] + " " + conf['mqtt_password']

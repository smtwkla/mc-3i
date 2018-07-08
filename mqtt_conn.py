
import mqtt_config

conf=mqtt_config.read_mqtt_conf()

print "config:"
print conf['mqtt_host'] + " " + conf['mqtt_port'] + " " +  conf['mqtt_username'] + " " + conf['mqtt_password']

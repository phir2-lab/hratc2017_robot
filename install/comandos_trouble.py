#!/bin/sh

import paho.mqtt.client as mqtt
import os

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Daleee!!")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("cmd_trouble")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	s = str(msg.payload)
	if (s == "shutdown"):
		os.system("sudo shutdown -h 0");

	if(s == "reset"):
		os.system("sudo reboot");

	if(s == "stop"):
		os.system("sudo killall -9 teleop");

	else :
		print (s)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.42.0.1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
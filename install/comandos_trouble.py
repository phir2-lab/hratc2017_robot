#!/bin/sh
# Description: this is script is an alternative way (via mqtt) to access the robot
# and execute commands such as : shutdown, reset, stop.
# Author: Renato

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
		# TODO: Renato, nao eh o suficiente matar este nodo.
		# na competicao cada equipe tera um nodo diferente.
		# acho melhor mandar stop no cmdvel ou matar o todo o ROS
		os.system("sudo killall -9 teleop");

	else :
		print (s)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# TODO: este IP é mesmo fixo 
client.connect("10.42.0.1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

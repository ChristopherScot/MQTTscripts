import paho.mqtt.client as mqtt
from subprocess import call

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("AmHome/Chris")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if str(msg.payload) == "1":
         print("This is where the message should play")
         call(["mpg123", "/home/pi/audiofiles/home.mp3"])
    elif str(msg.payload) =="0" :
         print("Not Home Anymore")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("c2smart.asuscomm.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

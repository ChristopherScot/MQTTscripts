import paho.mqtt.client as mqtt
from subprocess import call

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('pilight433/#')
    call(["service", "pilight", "restart"])
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if (msg.topic == "pilight433/Light") :
        if str(msg.payload) == "1" :
              print("Turn Light On")
              call(["pilight-send", "-p", "clarus_switch", "-i", "A2", "-u", "36", "-t"])
        elif str(msg.payload) =="0" :
              call(["pilight-send", "-p", "clarus_switch", "-i", "A2", "-u", "36", "-f"])
              print("Turn Light Off")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("c2smart.asuscomm.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

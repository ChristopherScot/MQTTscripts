
# Import standard python modules.
import random
import sys
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient
# Import call so I can run commandline arguments
from subprocess import call


# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = '155a42c36fc24988a977a41204e2835f'
ADAFRUIT_IO_USERNAME = 'c2smart'  # See https://accounts.adafruit.com
                                                    # to find your username.


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for changes...')
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe('Lights')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
	print('Feed {0} received new value: {1}'.format(feed_id, payload))
	if str(payload) == "Bedroom on" :
		print("Turn Light On")
		call(["pilight-send", "-p", "clarus_switch", "-i", "A2", "-u", "36", "-t"])
	elif str(payload) =="Bedroom off" :
		call(["pilight-send", "-p", "clarus_switch", "-i", "A2", "-u", "36", "-f"])
		print("Turn Light Off")

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_blocking()

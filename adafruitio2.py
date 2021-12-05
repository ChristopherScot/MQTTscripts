# Import library and create instance of REST client.
from Adafruit_IO import Client
from subprocess import call

aio = Client('155a42c36fc24988a977a41204e2835f')

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data = aio.receive('Lights')
if str(data.value) == "Bedroom on" :
	print("Turn Light On")
	call(["pilight-send", "-p", "clarus_switch", "-i", "A2", "-u", "36", "-t"])
elif str(data.value) =="Bedroom off" :
	call(["pilight-send", "-p", "clarus_switch", "-i", "A2", "-u", "36", "-f"])
	print("Turn Light Off")

print('Received value: {0}'.format(data.value))

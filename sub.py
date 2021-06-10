import paho.mqtt.client as paho
import time

broker = "127.0.0.1"
topic = "test"


def on_message(client, userdata, message):
    print("received data is :")
    print(str(message.payload.decode()))


client = paho.Client("user")
client.on_message = on_message

print("connecting to broker host", broker)
client.connect(broker)
print("subscribing begins here")
client.subscribe(topic)

while 1:
    client.loop_forever()

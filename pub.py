import paho.mqtt.client as paho
import time

broker = "127.0.0.1"
topic = "test"
port = 1883


def on_publish(client, userdata, result):
  print("published data is : ")
  pass

client1 = paho.Client("control1")
client1.on_publish = on_publish
client1.connect(broker, port, keepalive=60)


while True:
  payload = "Hiiii"
  ret= client1.publish(topic, payload)
  print(payload);
  print("Please check data on your Subscriber Code \n")
  time.sleep(5)

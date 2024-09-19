import random
import time
import threading
import paho.mqtt.client as paho
from paho.mqtt.subscribeoptions import SubscribeOptions

client_id = f'python-mqtt-{random.randint(0, 1000)}'
broker = "rule28.i4t.swin.edu.au"
port = 1883
username = "103501849"
password = "103501849"
topic = "public/hello"
topic2 = "103501849/test"
subtop = "public/#"
subtop2 = "103501849/+"

# Create a queue for user input
user_input_queue = []
utopic = []
ack = "Do you want me to authenticate you?"


def get_user_input():
    while True:
        user_topic = input("Enter user topic: ")
        if user_topic:
            utopic.append(user_topic)


def get_topic():
    while True:
        user_topic = input("Enter user topic: ")
        if user_topic:
            utopic.append(user_topic)


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n" % rc)

    client = paho.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, ack):
   # time.sleep(1)
    onlyonce = 0
    msg = ack

    # tp = utopic.pop(0)


    result2 = client.publish(topic2, msg)

    status2 = result2[0]
    if status2 == paho.MQTT_ERR_SUCCESS:
       # print(f"Sent '{msg}' to topic '{topic}'")
        print(f"Sent '{msg}' to topic '{topic2}'")
    else:
        print(f"Failed to send message")
    time.sleep(1)


def subscribe(client):
    def on_message(client1, userdata, msg):

        print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
        # print(f"{userdata} and {client}")
        resp = msg.payload.decode()
        res_str = resp.split('"')
        print(res_str)
        if len(res_str) > 4:
            sep = res_str[3].split(":")
            print(sep)
            if sep[0] == 'ForYou':
                publish(client1, "Authenticated")

    client.subscribe(subtop)
    publish(client, "Do you want me to authenticate you?")
    client.subscribe(subtop2)
    client.on_message = on_message
    time.sleep(1)


def run():
    client = connect_mqtt()

 #   client.loop_start()
    # Start a separate thread for user input
    subscribe(client)
    client.loop_forever()


if __name__ == "__main__":
    run()

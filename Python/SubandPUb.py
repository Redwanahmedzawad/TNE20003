import random
import time
import threading
import paho.mqtt.client as paho

client_id = f'python-mqtt-{random.randint(0, 1000)}'
broker = "rule28.i4t.swin.edu.au"
port = 1883
username = "103501849"
password = "103501849"
topic = "public/hello"
topic2 = "103501849/test"
subtop = "public/#"
subtop2 = "103501849/#"

# Create a queue for user input
user_input_queue = []


def get_user_input():
    while True:
        user_msg = input("Enter a message to publish or press Enter to skip: ")
        if user_msg:
            user_input_queue.append(user_msg)


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


def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        if user_input_queue:
            msg = user_input_queue.pop(0)
            result = client.publish(topic, msg)
            result2 = client.publish(topic2, msg)
            status = result[0]
            status2 = result2[0]
            if status == paho.MQTT_ERR_SUCCESS and status2 == paho.MQTT_ERR_SUCCESS:
                print(f"Sent '{msg}' to topic '{topic}'")
                print(f"Sent '{msg}' to topic '{topic2}'")
            else:
                print(f"Failed to send message")
        msg_count += 1


def subscribe(client):
    def on_message(client, userdata, msg):
        if msg.topic != f"103501849/test/{client_id}":
            print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")

    client.subscribe(subtop)
    client.subscribe(subtop2)
    client.on_message = on_message
    time.sleep(1)


def run():
    client = connect_mqtt()
    client.loop_start()

    # Start a separate thread for user input
    input_thread = threading.Thread(target=get_user_input)
    input_thread.daemon = True
    input_thread.start()

    thread1 = threading.Thread(target=publish, args=(client,))
    thread2 = threading.Thread(target=subscribe, args=(client,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    client.loop_forever()


if __name__ == "__main__":
    run()

import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker Details
broker_address = "rule28.i4t.swin.edu.au"
username = "103524286"
password = "103524286"

# Create a MQTT client (Publisher)
client = mqtt.Client("Publisher")

# Create a MQTT client (Subscriber)
subscriber = mqtt.Client("Subscriber")

# Connect both clients to the broker
client.username_pw_set(username, password)
subscriber.username_pw_set(username, password)

client.connect(broker_address)
subscriber.connect(broker_address)

# Subscribe the subscriber to specific topics
subscriber_topic = f"{username}/my_private_topic"
new_topic = f"{username}/my_private_topic/MOE"  # Create a new topic
subscriber.subscribe([(subscriber_topic, 0), (new_topic, 0)])


while True:
    # Simulate data generation 
    voltage = random.uniform(0.65, 100.56)  # Replace with your data source

    # Publish data to a private topic
    publisher_topic = f"{username}/my_private_topic"
    client.publish(publisher_topic, f"Voltage: {voltage:.1f}")
    client.publish(publisher_topic, "What more should we do")

    # Publish data to the public topic
    public_topic = "public"
    client.publish(public_topic, f"Voltage: {voltage:.1f}")

    # Publish data to the new topic
    client.publish(new_topic, "This is my Sub Topic")

    time.sleep(3)  # Publish data every 3 seconds

# Disconnect both clients from the broker when done
client.disconnect()
subscriber.disconnect()

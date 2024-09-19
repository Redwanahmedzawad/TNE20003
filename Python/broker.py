import paho.mqtt.client as mqtt

# Set your credentials
username = "103501849"  # Replace with your student ID
password = "103501849"  # Replace with your student ID

# Set the MQTT broker address
broker_address = "rule28.i4t.swin.edu.au"
private_topic = "hello"  # Change to your private topic
public_topic = "#"  # Subscribe to all public topics

# Create an MQTT client instance
client = mqtt.Client()

# Set the username and password
client.username_pw_set(username, password)

# Define the on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the private and public topics
    client.subscribe(private_topic)
    client.subscribe(public_topic)

# Define the on_message callback
def on_message(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload.decode()}")

# Set the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, 1883)  # 1883 is the default MQTT port

# Start the MQTT client loop
client.loop_forever()

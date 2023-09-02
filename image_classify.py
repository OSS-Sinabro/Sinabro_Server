import os
import paho.mqtt.client as mqtt
from image_processing import classify_image
from config import MQTT_BROKER_ADDRESS, MQTT_PORT, BASE_IMAGE_PATH, TOPICS

print("****************************************************")
print("                     이미지 분류                     ")
print("****************************************************")

# Image save path
if not os.path.exists(BASE_IMAGE_PATH):
    os.makedirs(BASE_IMAGE_PATH)

# Function to save the image
def check_image(topic, image_data):
    try:
        # Start the image classification task
        classify_image(topic, image_data)

    except Exception as e:
        print("Error occurred while classifying image:", e)

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("                   Broker 연결성공                     \n")
        # config.py에서 가져온 TOPICS로 구독
        for topic in TOPICS:
            client.subscribe(topic, qos=0)
    else:
        print("Connection failed")

def on_message(client, userdata, msg):
    # 토픽을 확인하고, 해당 토픽에 맞게 이미지를 저장
    if "cctv_" in msg.topic:
        image_data = msg.payload
        check_image(msg.topic, image_data)  # check_image 함수에 토픽, 이미지 데이터 전달

# MQTT Client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER_ADDRESS, MQTT_PORT)

# Start the MQTT loop
client.loop_forever()

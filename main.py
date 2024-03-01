from Adafruit_IO import Client, Feed
import time
from uart import readSerial
from simple_ai import image_detector
AIO_FEED_ID = ["nutnhan1","nutnhan2"]
HOST = "tcp://io.adafruit.com"
AIO_USERNAME = "phucmychau"
AIO_KEY = "aio_dwGH66grOCJY3GgRUHoBfSnOFPhw"
counter_ai = 5
ai_result = ""
previous_result = ""
# def connected(client):
#     print("Ket noi thanh cong ...")
#     for topic in AIO_FEED_ID:
#         client.subscribe(topic)

# def subscribe(client , userdata , mid , granted_qos):
#     print("Subscribe thanh cong ...")

# def disconnected(client):
#     print("Ngat ket noi ...")
#     sys.exit (1)

# def message(client , feed_id , payload):
#     print("Nhan du lieu: " + payload)

# client = MQTTClient(AIO_USERNAME , AIO_KEY)
# # client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe
# client.connect()
# client.loop_background()
# counter = 10
client = Client(AIO_USERNAME, AIO_KEY)
# test = client.feeds("nutnhan1")
client.send_data("nutnhan1", 21)
while True:
    counter_ai = counter_ai - 1
    if counter_ai <= 0 :
        # todo for AI
        counter_ai = 5
        previous_result = ai_result
        ai_result = image_detector()
        print("AI Output: ", ai_result)
        if previous_result != ai_result:
            client.send_data("ai",ai_result[2:])
    # readSerial(client)
    time.sleep(1)
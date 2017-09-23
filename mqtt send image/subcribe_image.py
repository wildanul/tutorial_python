import paho.mqtt.client as mqtt

# Define on_connect event Handler
#def on_connect(mosq, obj, rc):
#	#Subscribe to a the Topic
#	mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
#def on_subscribe(mosq, obj, mid, granted_qos):
#    print "Subscribed to MQTT Topic"

# Define on_message event Handler
#def on_message(mosq, obj, msg):
#	print msg.payload

def on_connect(client, userdata, rc):
    print("Connect" + str(rc))
    client.subscribe("testTopic")

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"
    
def on_message(client, userdata, msg):
    print "Topic : ", msg.topic
    f = open("output.jpg", "wb")  #there is a output.jpg which is different
    #f = open("output.png", "wb")  #there is a output.jpg which is different
    f.write(msg.payload)
    f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.connect("s0.iotnesia.com", 1883, 60)

client.loop_forever()

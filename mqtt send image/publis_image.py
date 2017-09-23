#'''
import paho.mqtt.client as mqtt

#def on_publish(mosq, userdata, mid):
#    mosq.disconnect()

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	print "Connected to MQTT Broker"

# Define on_publish event Handler
def on_publish(client, userdata, mid):
	print "Message Published..."    

# Initiate MQTT Client
client = mqtt.Client()

# Register Event Handlers
client.on_publish = on_publish
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)#free broker mqtt
#client.on_publish = on_publish

#f=open("C:\Users\wildan\Desktop\1.png", "rb") #3.7kiB in same folder
f=open("input.jpg", "rb") #3.7kiB in same folder
fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish("testTopic",byteArr,0)
print('aaaaaa')
print(fileContent)
print(byteArr)
client.loop_forever()

'''
import paho.mqtt.client as mqtt

def on_publish(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client()
client.username_pw_set('user', 'password')
client.>

client.connect("myvps.com", 1883, 60)

f = open('1.jpg', 'rb')
fileContent = f.read()
byteArr = bytes(fileContent)
client.publish("test", byteArr, 0)

client.loop_forever()
'''

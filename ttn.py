import paho.mqtt.client as mqtt
import json
 
# O retorno de chamada para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('+/devices/+/up')
 
# O retorno de chamada para quando uma mensagem PUBLISH é recebida do servidor.
def on_message(client, userdata, msg):
    mensagem = json.loads(msg.payload)
    values = mensagem['payload_fields']
    print(values)
    #print(values['contador'])
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.tls_set()
client.username_pw_set('1app1',password='ttn-account-v2.Po1PPfSFy-13u3Fls_UV8VGAOud4YDTfzVjyyvPb4GM')
 
client.connect('brazil.thethings.network', 8883, 60)
 
client.loop_forever()
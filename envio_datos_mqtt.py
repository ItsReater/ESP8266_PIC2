import paho.mqtt.client as mqtt

# Definir los parametros de conexión.
broker = "localhost"
port = 1883
topic1 = "pic2/temperature"
topic2 = "pic2/humidity"

# Definimos un callback
def on_connect(client, userdata, flag, rc):
    print(f"Me he conectado al broker MQTT Mosquitto!")
    temperature = 22.5
    client.publish(topic1, str(temperature))

#Crear un cliente MQTT
client = mqtt.Client()

# Asignamos la función callback para la conexión
client.on_connect = on_connect

# Conectar al broker
client.connect(broker, port, 60)
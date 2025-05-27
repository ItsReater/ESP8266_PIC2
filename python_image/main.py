import paho.mqtt.client as mqtt

# Definimos un callback
def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Connected to the MQTT broker!"+str(rc))
        client.subscribe("pic2/#")
    else:
        print("ERROR in connection.")

def on_message(client, userdata, msg):
    # Recibimos los datos, luego hay que pasarlos a base de datos.
    print(msg.topic+" "+str(msg.payload.decode()))
    print(f"\n {type(msg.payload.decode())}")
    if msg.topic == "pic2/temperature":
        pass
    elif msg.topic =="pic2/humidity":
        pass

if __name__ == "__main__":

    broker = "localhost"
    port = 1883

    #Crear un cliente MQTT
    client = mqtt.Client()

    # Asignamos la función callback para la conexión
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar al broker
    client.connect(broker, port, 60)

    # Dejar conexión en loop.
    client.loop_forever()

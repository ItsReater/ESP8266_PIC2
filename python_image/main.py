import paho.mqtt.client as mqtt
import psycopg2
from datetime import datetime

# Variables globales para temperatura y humedad
last_temp = None
last_hum = None

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host="db",
    database="mydb",
    user="user",
    password="pass"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS readings (
        id SERIAL PRIMARY KEY,
        plc_id VARCHAR(50),
        timestamp TIMESTAMP,
        temperature REAL,
        humidity REAL
    );
""")
conn.commit()

def save_to_db(plc_id, temperature, humidity):
    now = datetime.now()
    query = "INSERT INTO readings (plc_id, timestamp, temperature, humidity) VALUES (%s, %s, %s, %s);"
    values = (plc_id, now, temperature, humidity)
    cursor.execute(query, values)
    conn.commit()
    print(f"Inserted into DB: {plc_id}, {now}, {temperature}, {humidity}")


# Definimos un callback
def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Connected to the MQTT broker!"+str(rc))
        client.subscribe("pic2/#")
    else:
        print("ERROR in connection.")

def on_message(client, userdata, msg):
    global last_hum, last_temp
    # Recibimos los datos, luego hay que pasarlos a base de datos.
    print(msg.topic+" "+str(msg.payload.decode()))
    print(f"\n {type(msg.payload.decode())}")

    topic = msg.topic
    payload = msg.payload.decode()

    try:
        value = float(payload)
    except ValueError:
        print("Could not convert payload to float.")
        return
    
    if topic == "pic2/temperature":
        last_temp = value
    elif topic == "pic2/humidity":
        last_hum = value
        if last_temp is not None:
            save_to_db("ESP8266", last_temp, last_hum)
            # Limpiamos valores.
            last_temp = None
            last_hum = None

if __name__ == "__main__":

    broker = "mosquitto"
    port = 1883

    #Crear un cliente MQTT
    client = mqtt.Client()

    # Asignamos la función callback para la conexión
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar al broker
    client.connect(broker, port, 60)

    print("MQTT Client initialized and connecting...")

    # Dejar conexión en loop.
    client.loop_forever()

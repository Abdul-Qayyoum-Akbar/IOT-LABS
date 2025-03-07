from machine import Pin
from dht import DHT22
import time
import network
import blynklib
import Blynk

# Replace with your Wi-Fi credentials
WIFI_SSID = 'NTU FSD'
WIFI_PASSWORD = ''

# Replace with your Blynk Auth Token
BLYNK_AUTH_TOKEN = 'YyL4A_mIEBqPxOJTRlHxdHgqVv_0in_2'

# Initialize DHT22 sensor (e.g., connected to Pin 14)
dht_sensor = DHT11(Pin(14))

# Connect to Wi-Fi
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        print('Connecting to WiFi...')
        wifi.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wifi.isconnected():
            pass
    print('Connected to WiFi:', wifi.ifconfig())

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH_TOKEN)

def read_sensor_and_send():
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        print('Temperature:', temp, '°C')
        print('Humidity:', humidity, '%')

        # Send data to Blynk
        blynk.virtual_write(0, temp)  # Send temperature to V0
        blynk.virtual_write(1, humidity)  # Send humidity to V1
    except Exception as e:
        print('Failed to read sensor:', e)

# Connect to Wi-Fi
connect_wifi()

# Run the Blynk loop
while True:
    blynk.run()
    read_sensor_and_send()
    time.sleep(5)  # Send data every 5 seconds

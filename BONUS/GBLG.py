import network
import time
import BlynkLib
from machine import Pin, I2C
from neopixel import NeoPixel
import ssd1306

# Wi-Fi Credentials
WIFI_SSID = "NTU FSD"
WIFI_PASS = ""

# Blynk Auth Token
BLYNK_AUTH = "HQfUeeVUaziWBFULK79qAJjtVPPqAjp5"

# OLED Display Setup
I2C_SCL = 9  # Adjust based on your board
I2C_SDA = 8  # Adjust based on your board
i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def display_text(text):
    oled.fill(0)  # Clear screen
    oled.text(text, 10, 30)
    oled.show()

# Built-in RGB LED on GPIO 48
RGB_PIN = 48
NUM_LEDS = 1  # Only one built-in LED
rgb_led = NeoPixel(Pin(RGB_PIN, Pin.OUT), NUM_LEDS)

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)

    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(1)

    print("Connected to Wi-Fi:", wlan.ifconfig())

connect_wifi()

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Function to control RGB LED
def set_color(r, g, b):
    rgb_led[0] = (r, g, b)
    rgb_led.write()

# Blynk Button Handlers
@blynk.on("V0")  # Button for Red
def v0_write(value):
    if int(value[0]) == 1:
        set_color(255, 0, 0)  # Red ON
        display_text("Red ON")
    else:
        set_color(0, 0, 0)  # OFF
        display_text("Red OFF")

@blynk.on("V1")  # Button for Green
def v1_write(value):
    if int(value[0]) == 1:
        set_color(0, 255, 0)  # Green ON
        display_text("Green ON")
    else:
        set_color(0, 0, 0)  # OFF
        display_text("Green OFF")

@blynk.on("V2")  # Button for Blue
def v3_write(value):
    if int(value[0]) == 1:
        set_color(0, 0, 255)  # Blue ON
        display_text("Blue ON")
    else:
        set_color(0, 0, 0)  # OFF
        display_text("Blue OFF")

@blynk.on("V3")  # Button for White
def v4_write(value):
    if int(value[0]) == 1:
        set_color(255, 255, 0)  # White ON
        display_text("Yellow ON")
    else:
        set_color(0, 0, 0)  # OFF
        display_text("Yellow OFF")



# Main Loop
while True:
    blynk.run()

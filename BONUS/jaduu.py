import network
import time

SSID = "NTU FSD"
PASSWORD = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

for _ in range(15):  # Wait for 15 seconds
    if wlan.isconnected():
        print("✅ Connected! IP Address:", wlan.ifconfig()[0])
        break
    print("⏳ Connecting...")
    time.sleep(1)

if not wlan.isconnected():
    print("❌ Failed to connect. Check credentials and try again.")
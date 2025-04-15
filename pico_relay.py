from machine import Pin
import network
import time
try:
    import usocket as socket
except:
    import socket

relay = Pin(18, Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("NAMA_WIFI", "PASSWORD_WIFI")

# Tunggu koneksi WiFi
while not wlan.isconnected():
    print("Menghubungkan WiFi...")
    time.sleep(1)

ip = wlan.ifconfig()[0]
print("Terhubung dengan IP:", ip)

def handle_request(request):
    if '/relay=on' in request:
        relay.value(0)
        return "Relay ON"
    elif '/relay=off' in request:
        relay.value(1)
        return "Relay OFF"
    else:
        return "Perintah tidak dikenali"

# Web server hanya sebagai endpoint API
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Koneksi dari:", addr)
    request = conn.recv(1024).decode()
    print("Request:", request)
    
    response_body = handle_request(request)

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n" + response_body
    conn.send(response.encode())
    conn.close()

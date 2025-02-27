import serial
ser = serial.Serial('COM3', 115200)  # Change COM3 to your ESP32 port
while True:
    data = ser.readline().decode().strip()
    print(f"Received from ESP32: {data}")

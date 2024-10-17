import serial
import time

PORT = 'COM5'
BAUDRATE = 9600
ser = serial.Serial(PORT, BAUDRATE)
time.sleep(3)  # Allow time for the connection to establish
thres = 200

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print(data)
        parts = data.split()
        print(parts)
        R = parts[1]
        G = parts[3]
        B = parts[5]
        redPW = int(R)
        greenPW = int(G)
        bluePW = int(B)
        if redPW < thres and greenPW < thres and bluePW < thres:
            print("White")
        elif redPW > thres and greenPW > thres and bluePW > thres:
            print("Detected: Black")
        elif redPW < thres and greenPW > thres and bluePW > thres:
            print("Detected: Red")
        elif greenPW < thres and redPW > thres and bluePW > thres:
            print("Detected: Green")
        elif bluePW < thres and greenPW > thres and redPW > thres:
            print("Detected: Blue")
        else:
            print("No dominant color detected")
    time.sleep(0.5)

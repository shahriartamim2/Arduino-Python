import serial
import time

# Replace 'COM5' with your Arduino's COM port
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(1)  # Allow time for the connection to establish

while True:
    line = arduino.readline().decode(errors='ignore').strip() 
    print(f"Raw output: {line}")
    time.sleep(0.7)  # Delay between readings
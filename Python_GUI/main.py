import serial
import time

# Replace 'COM3' with your Arduino's COM port (e.g., 'COM4' for Windows or '/dev/ttyUSB0' for Linux)
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

threshold = 200

def read_color():
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        if line:
            print(line)
            # Parse the values from the serial line
            try:
                parts = line.split()
                redPW = int(parts[0].split(':')[1])
                greenPW = int(parts[1].split(':')[1])
                bluePW = int(parts[2].split(':')[1])
                return redPW, greenPW, bluePW
            except (IndexError, ValueError):
                print("Error parsing data")

    return None, None, None

def determine_color(redPW, greenPW, bluePW):
    if redPW < threshold and greenPW < threshold and bluePW < threshold:
        return "Detected: White"
    elif redPW > threshold and greenPW > threshold and bluePW > threshold:
        return "Detected: Black"
    elif redPW < threshold and greenPW > threshold and bluePW > threshold:
        return "Detected: Red"
    elif greenPW < threshold and redPW > threshold and bluePW > threshold:
        return "Detected: Green"
    elif bluePW < threshold and greenPW > threshold and redPW > threshold:
        return "Detected: Blue"
    else:
        return "No dominant color detected"

try:
    while True:
        redPW, greenPW, bluePW = read_color()
        if redPW is not None:
            color = determine_color(redPW, greenPW, bluePW)
            print(color)
        time.sleep(0.5)  # Delay between readings

except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    arduino.close()
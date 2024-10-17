import serial
import time

# Replace 'COM5' with your Arduino's COM port
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

threshold = 200

def read_color():
    if arduino.in_waiting > 0:
        line = arduino.readline().decode(errors='ignore').strip()  # Decode and ignore errors if any non-UTF characters are encountered
        print(f"Raw output: {line}")
        if line:
            print(f"Raw output: {line}")
            try:
                # Parse the values from the serial line (e.g., "R:123 G:456 B:789")
                parts = line.split()
                if len(parts) == 3:
                    # Extract values from each part
                    red_str = parts[0].split(':')
                    green_str = parts[1].split(':')
                    blue_str = parts[2].split(':')

                    # Check if each part has a valid value after splitting
                    if len(red_str) == 2 and len(green_str) == 2 and len(blue_str) == 2:
                        redPW = int(red_str[1])
                        greenPW = int(green_str[1])
                        bluePW = int(blue_str[1])
                        return redPW, greenPW, bluePW
                    else:
                        print("Error: Missing color values in the input")
                else:
                    print("Error: Unexpected format of input")
            except (IndexError, ValueError) as e:
                print(f"Error during parsing: {e}")

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
        if redPW is not None and greenPW is not None and bluePW is not None:
            color = determine_color(redPW, greenPW, bluePW)
            print(color)
        time.sleep(0.5)  # Delay between readings

except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    arduino.close()

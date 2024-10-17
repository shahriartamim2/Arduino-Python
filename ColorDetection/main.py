import serial
import time
import bobbin_color

selectedColor = bobbin_color.selectedColor

PORT = 'COM5'
BAUDRATE = 9600
ser = serial.Serial(PORT, BAUDRATE)
time.sleep(3)  # Allow time for the connection to establish
thres = 200
detectedColor = ""

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print(data)
        parts = data.split()
        R = parts[1]
        G = parts[3]
        B = parts[5]
        redPW = int(R)
        greenPW = int(G)
        bluePW = int(B)
        if redPW < thres and greenPW < thres and bluePW < thres:
            detectedColor = "White"
            print(f"{detectedColor} color detected")
            if detectedColor == selectedColor:
                print("Bobbin color matched with selected color")
            else:
                print("Bobbin color did not match with selected color. Please change the bobbin.")
        elif redPW > thres and greenPW > thres and bluePW > thres:
            detectedColor = "Black"
            print(f"{detectedColor} color detected")
            if detectedColor == selectedColor:
                print("Bobbin color matched with selected color")
            else:
                print("Bobbin color did not match with selected color. Please change the bobbin.")
        elif redPW < thres and greenPW > thres and bluePW > thres:
            detectedColor = "Red"
            print(f"{detectedColor} color detected")
            if detectedColor == selectedColor:
                print("Bobbin color matched with selected color")
            else:
                print("Bobbin color did not match with selected color. Please change the bobbin.")
        elif greenPW < thres and redPW > thres and bluePW > thres:
            detectedColor = "Green"
            print(f"{detectedColor} color detected")
            if detectedColor == selectedColor:
                print("Bobbin color matched with selected color")
            else:
                print("Bobbin color did not match with selected color. Please change the bobbin.")
        elif bluePW < thres and greenPW > thres and redPW > thres:
            detectedColor = "Blue"
            print(f"{detectedColor} color detected")
            if detectedColor == selectedColor:
                print("Bobbin color matched with selected color")
            else:
                print("Bobbin color did not match with selected color. Please change the bobbin.")
        else:
            print("No dominant color detected")
    time.sleep(0.5)

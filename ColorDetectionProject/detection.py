import tkinter as tk
from tkinter import Label
import serial
import time
import bobbin_color

# Initialize serial communication and variables
bobbinColor = bobbin_color.selectedColor  # Preselected color from the other module
detectedColor = ""

PORT = 'COM5'
BAUDRATE = 9600
ser = serial.Serial(PORT, BAUDRATE)
time.sleep(3)  # Allow time for the connection to establish
thres = 200

# Function to update the detected color label and match status
def update_gui(second_window, detected_color_label, match_status_label):
    global detectedColor

    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        parts = data.split()
        
        if len(parts) >= 6:  # Ensure the expected format
            R = parts[1]
            G = parts[3]
            B = parts[5]
            redPW = int(R)
            greenPW = int(G)
            bluePW = int(B)

            # Detect color based on PWM thresholds
            if redPW < thres and greenPW < thres and bluePW < thres:
                detectedColor = "White"
            elif redPW > thres and greenPW > thres and bluePW > thres:
                detectedColor = "Black"
            elif redPW < thres and greenPW > thres and bluePW > thres:
                detectedColor = "Red"
            elif greenPW < thres and redPW > thres and bluePW > thres:
                detectedColor = "Green"
            elif bluePW < thres and greenPW > thres and redPW > thres:
                detectedColor = "Blue"
            else:
                detectedColor = "No dominant color detected"

            # Update the detected color label
            detected_color_label.config(text=f"Detected Color: {detectedColor}")
            
            # Check if the detected color matches the selected bobbin color
            if detectedColor == bobbinColor:
                match_status_label.config(text="Match Status: Matched", fg="green")
            else:
                match_status_label.config(text="Match Status: Mismatch", fg="red")
        
    # Schedule the function to run again after a short delay
    second_window.after(500, lambda: update_gui(second_window, detected_color_label, match_status_label))

# Function to create and display the detection window
def create_detection_window():
    # Create a new window for the detection process
    second_window = tk.Toplevel()
    second_window.title("Color Detection")
    second_window.geometry("400x300")

    # Create Labels to display the detected color and match status
    detected_color_label = Label(second_window, text="Detected Color: None", font=("Arial", 14))
    detected_color_label.pack(pady=10)

    match_status_label = Label(second_window, text="Match Status: Not Checked", font=("Arial", 14))
    match_status_label.pack(pady=10)

    # Start the detection process by calling update_gui
    update_gui(second_window, detected_color_label, match_status_label)

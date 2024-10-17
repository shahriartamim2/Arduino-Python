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

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("Color Detection")
root.geometry("700x300")

# Create Labels to display the detected color and match status
detected_color_label = Label(root, text="Detected Color: None", font=("Arial", 14))
detected_color_label.pack(pady=10)

match_status_label = Label(root, text="Match Status: Not Checked", font=("Arial", 14))
match_status_label.pack(pady=10)

# Function to update the detected color label and match status
def update_gui():
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
                match_status_label.config(text="Bobbin color Matched", fg="green")
            else:
                match_status_label.config(text=f"Bobbin color does not Match. Please insert '{bobbinColor}' Bobbin", fg="red")
        
    # Schedule the function to run again after a short delay
    root.after(500, update_gui)

# Start the GUI update loop
update_gui()

# Run the Tkinter main loop
root.mainloop()

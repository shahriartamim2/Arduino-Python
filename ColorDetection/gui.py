import tkinter as tk
import bobbin_color

# Function to update the label and selectedColor variable when a color button is clicked
def update_label(color):
    global bobbin_color
    bobbin_color.selectedColor = color  # Update the variable in the imported module
    label.config(text=f"Selected Color: {color}")

# Function to export the selected color (effectively updates the module)
def export_color():
    selectedColor = bobbin_color.selectedColor
    if selectedColor:
        with open("bobbin_color.py", "w") as file:
            file.write(f"selectedColor = '{selectedColor}'\n")
        label.config(text=f"Bobbin Color set to : {selectedColor}")
        print(f"Selected color '{selectedColor}' has been written to selected_color.py")
    else:
        print("No color selected to export.")


# Create the main window
root = tk.Tk()
root.title("Color Selection GUI")
root.geometry("500x350")

# Create a label widget
label = tk.Label(root, text="Select a Color", font=("Arial", 14))
label.pack(pady=20)

# Create color buttons
colors = ['Red', 'Green', 'Blue', 'Black', 'White']
for color in colors:
    button = tk.Button(
        root, 
        text=color, 
        command=lambda c=color: update_label(c), 
        width=10, 
        bg=color.lower(),  # Set the button background color
        fg="white" if color in ['Black', 'Blue'] else "black"  # Set text color for better contrast
    )
    button.pack(pady=5)

# Create an "Export" button to save the selected color
export_button = tk.Button(root, text="Export Color", command=export_color)
export_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()


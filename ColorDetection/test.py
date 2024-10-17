# Import the selectedColor from selected_color module
import bobbin_color

# Example usage
if __name__ == "__main__":
    selected_color_value = bobbin_color.selectedColor
    if selected_color_value:
        print(f"The imported selected color is: {selected_color_value}")
    else:
        print("No color has been selected yet.")

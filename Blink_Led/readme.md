# Blink LED with Python and Arduino

This project demonstrates how to control an LED using Python and an Arduino board via the `pyfirmata2` library.

## Features

- Control an LED connected to an Arduino.
- Uses the Firmata protocol for communication with Python.

## Requirements

- Arduino IDE (to upload Firmata)
- Python 3.x
- `pyfirmata2` library
- Arduino (e.g., Uno)
- LED, resistor, jumper wires

## Setup

### Step 1: Install Python Dependencies

1. Create a virtual environment:
   ```bash
   python -m venv myenv
```

2.  Activate the environment:
   ```bash
   myenv\Scripts\activate
```

3. Install pyfirmata2:
   ```bash
   pip install pyfirmata2
```

### Step 2: Upload Firmata to Arduino
 1.Open Arduino IDE.
 2.Upload StandardFirmata from File > Examples > Firmata.

### Step 4: Run the Python Script

Run the script to control the LED:
   ```bash
   python src/blinkLed.py
```



import tkinter as tk
from tkinter import messagebox
from backend_script import arg_parse, vehicle_detection_function

# Function to start vehicle detection
def start_detection():
    try:
        args = arg_parse()
        # Call the function from the backend script for vehicle detection
        vehicle_info = vehicle_detection_function(args)
        # Update labels with vehicle information
        signal_label["text"] = f"Signal: Green"  # Assuming the signal is green initially
        lane_label["text"] = f"Lane: {vehicle_info['denser_lane']}"
        countdown_label["text"] = f"Countdown: {vehicle_info['vehicle_count']}"
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create a Tkinter window
window = tk.Tk()
window.title("Intelligent Traffic Management System")

# Create labels for signals and lanes
signal_label = tk.Label(window, text="Signal: Green", fg="green", font=("Arial", 24))
signal_label.pack()

lane_label = tk.Label(window, text="Lane: 1", fg="green", font=("Arial", 24))
lane_label.pack()

# Create a countdown label
countdown_label = tk.Label(window, text="Countdown: 10", font=("Arial", 24))
countdown_label.pack()

# Create a button to start detection
start_detection_button = tk.Button(window, text="Start Detection", command=start_detection)
start_detection_button.pack()

# Run the Tkinter event loop
window.mainloop()

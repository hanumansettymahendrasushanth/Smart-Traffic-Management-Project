import tkinter as tk
from tkinter import scrolledtext
import subprocess

def run_script():
    # Run the Python script and capture its output
    result = subprocess.run(['python', 'itms-yolov3.py'], capture_output=True, text=True)
    output_text.insert(tk.END, result.stdout)

# Create the main window
root = tk.Tk()
root.title("Python Script Output")

# Add a text area for displaying the output
output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack()

# Add a button to run the script
run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.pack()

# Start the GUI event loop
root.mainloop()
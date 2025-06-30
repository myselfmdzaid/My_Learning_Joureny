# import necessary libraries
import tkinter as tk
from time import strftime
from datetime import datetime

# Create the main window
root = tk.Tk()

root.geometry("600x300")
root.configure(bg="#1E1E1E")  # dark background
root.resizable(0, 0)

# Add a title label
title_label = tk.Label(root, text="Digital Clock", font=('Segoe UI', 20, 'bold'), fg='white', bg="#1E1E1E")
title_label.pack(pady=(3, 5)) 

# Define the function to update time
def update_time():
    current_time = strftime('%I:%M:%S %p').lower()  # Format time as: 01:23:45 pm
    time_label.config(text=current_time) 

    # Format date as: June 27, 2025
    today = datetime.now() 
    current_date = today.strftime('%B %d, %Y') 
    date_label.config(text=current_date)

    time_label.after(1000, update_time)

# Styling for time
time_label = tk.Label(root, font=('Segoe UI', 50, 'bold'), fg='cyan', bg="#1E1E1E")
time_label.pack(pady=(30, 10))

# Styling for date
date_label = tk.Label(root, font=('Segoe UI', 30), fg='white', bg="#1E1E1E")
date_label.pack()

# Add a footer label
footer_label = tk.Label(root, text="Created by Mohammed Zaid", font=('Segoe UI', 12), fg='white', bg="#1E1E1E")
footer_label.pack(side=tk.BOTTOM, pady=(10, 0))


# Start the clock
update_time()
root.mainloop()

# Note: The code creates a digital clock using Tkinter, displaying the current time and date in a formatted manner.
# It updates every second and uses a label to show the time in a large, readable font
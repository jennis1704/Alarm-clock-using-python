import tkinter as tk
from datetime import datetime
import time
def check_alarm(alarm_time):
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            # Show a pop-up window or play a sound to notify the user
            print("ALARM!")
            break
        time.sleep(1)
def set_alarm():
    alarm_time = entry.get()
    check_alarm(alarm_time)

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (24-hour format HH:MM:SS):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()
root.mainloop()
import pyautogui
import numpy as np
import os
import cv2
import tkinter as tk


root = tk.Tk()

base_frame = tk.Frame(root)
base_frame.pack()


global record
record = False

# Record when True


def start_record(bool):
    global record
    record = bool

# Stop when False


def stop_record(bool):
    global record
    record = bool


name = 'test.avi'
image = pyautogui.screenshot()
frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
height, width, channels = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(name, fourcc, 20.0, (width, height))

while record == True:
    try:
        image = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        output.write(frame)
        StopIteration(0.5)
    except KeyboardInterrupt:
        break

output.release()
cv2.destroyAllWindows()


record_button = tk.Button(base_frame, text="Record", command=lambda *args: start_record(True))
record_button.pack()

stop_button = tk.Button(base_frame, text="Stop", command=lambda *args: stop_record(False))
stop_button.pack()

print_button = tk.Button(base_frame, text="Bool", command=lambda: print(record))
print_button.pack()

root.mainloop()

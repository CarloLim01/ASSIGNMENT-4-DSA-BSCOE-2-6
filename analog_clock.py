import tkinter as ui

import time
import math

window = ui.Tk()
window.geometry("400x400")

def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

canvas = ui.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill='both')

bg = ui.PhotoImage(file='dial_400.png')
canvas.create_image(200, 200, image=bg)

center_x = 200
center_y = 200

seconds_hand_len = 95
minutes_hand_len = 80
hours_hand_len = 60

seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')

minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')

hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')

update_clock()

window.mainloop()
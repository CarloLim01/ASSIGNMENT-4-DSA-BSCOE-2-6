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

update_clock()

window.mainloop()
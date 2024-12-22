#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas
from typing import Any

def start_motion(event: Any) -> None:
    global target_x, target_y
    target_x, target_y = event.x, event.y
    motion()

def motion() -> None:
    coords = c.coords(ball)
    current_x = (coords[0] + coords[2]) / 2
    current_y = (coords[1] + coords[3]) / 2

    dx = (target_x - current_x) * 0.1
    dy = (target_y - current_y) * 0.1

    c.move(ball, dx, dy)

    if (abs(current_x - target_x) > 1 or 
        abs(current_y - target_y) > 1):
        root.after(10, motion)

root = Tk()

c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')

c.bind('<Button-1>', start_motion)

target_x, target_y = 0, 0

root.mainloop()
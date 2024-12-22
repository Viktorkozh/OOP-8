#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas


root = Tk()
c = Canvas(root, width=200, height=200, bg="white")
c.pack()
c.create_rectangle(
    50, 70, 140, 170, fill="lightblue", outline="lightblue", width=3, activedash=(5, 4)
)
c.create_polygon(
    30, 70, 160, 70, 95, 20, fill="lightblue", outline="lightblue", width=3
)
c.create_oval(190, 20, 160, 50, fill="orange", outline="orange", width=3)

for i in range(000, 300, 10):
    c.create_line(i, 160, 
                  i - 5, 175, 
                  i - 10, 200, 
                  fill="green", 
                  width=2)

root.mainloop()

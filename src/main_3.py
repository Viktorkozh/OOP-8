#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Entry, Button, Text
from typing import Optional, Any


def change_text_size(event: Optional[Any] = None) -> None:
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        text_widget.config(width=width, height=height)
    except ValueError:
        pass


def focus_in(event: Any) -> None:
    event.widget.config(bg="white")


def focus_out(event: Any) -> None:
    event.widget.config(bg="lightgrey")


root: Tk = Tk()
root.title("Изменение размера текстового поля")

width_entry: Entry = Entry(root)
width_entry.pack()
width_entry.bind("<Return>", change_text_size)

height_entry: Entry = Entry(root)
height_entry.pack()
height_entry.bind("<Return>", change_text_size)

change_button: Button = Button(
    root,
    text="Изменить размер",
    command=change_text_size,
)
change_button.pack()

text_widget: Text = Text(root, width=30, height=10, bg="lightgrey")
text_widget.pack()
text_widget.bind("<FocusIn>", focus_in)
text_widget.bind("<FocusOut>", focus_out)

root.mainloop()

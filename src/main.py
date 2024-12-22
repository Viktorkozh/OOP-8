#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Listbox, Button, END, EXTENDED


def move_to_cart() -> None:
    selected_indices = goods_list.curselection()

    for index in reversed(selected_indices):
        item = goods_list.get(index)
        cart_list.insert(END, item)
        goods_list.delete(index)


def remove_from_cart() -> None:
    selected_indices = cart_list.curselection()

    for index in reversed(selected_indices):
        item = cart_list.get(index)
        goods_list.insert(END, item)
        cart_list.delete(index)


root = Tk()

frame = Frame(root)
frame.pack()

goods_list = Listbox(frame, width=30, height=10, selectmode=EXTENDED)
goods_list.grid(row=1, column=0)

goods = [
    "apple",
    "bananas",
    "carrot",
    "bread",
    "butter",
    "meat",
    "potato",
    "pineapple",
    "milk",
    "tomato",
]

for item in goods:
    goods_list.insert(END, item)

button_frame = Frame(frame)
button_frame.grid(row=1, column=1)

to_cart_btn = Button(button_frame, text=">>>", command=move_to_cart)
to_cart_btn.pack()

from_cart_btn = Button(button_frame, text="<<<", command=remove_from_cart)
from_cart_btn.pack()

cart_list = Listbox(frame, width=30, height=10, selectmode=EXTENDED)
cart_list.grid(row=1, column=2)

root.mainloop()

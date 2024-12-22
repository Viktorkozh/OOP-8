#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Listbox, END, EXTENDED, W, X, BOTH, Entry, Label


def add_to_list(event: None = None) -> None:
    text = entry.get().strip()

    if text:
        list_box.insert(END, text)
        entry.delete(0, END)


def copy_to_entry(event: None) -> None:
    try:
        selected_index = list_box.curselection()[0]
        selected_text = list_box.get(selected_index)

        entry.delete(0, END)
        entry.insert(0, selected_text)
    except IndexError:
        pass


root = Tk()

frame = Frame(root)
frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

label_entry = Label(frame, text="Введите текст:")
label_entry.pack(anchor=W)

entry = Entry(frame, width=50)
entry.pack(fill=X, pady=5)
entry.bind("<Return>", add_to_list)

label_list = Label(frame, text="Список:")
label_list.pack(anchor=W)

list_box = Listbox(frame, width=50, height=10, selectmode=EXTENDED)
list_box.pack(fill=BOTH, expand=True)

list_box.bind("<Double-Button-1>", copy_to_entry)

root.mainloop()

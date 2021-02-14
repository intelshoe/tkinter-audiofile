#!/usr/bin/env python3
'''
Main app entry point.

'''
import tkinter as tk
from window import Application

root = tk.Tk()
root.geometry("400x400")
app = Application(master=root)
app.mainloop()

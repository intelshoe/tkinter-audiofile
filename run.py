#!/usr/bin/env python3
'''
Main app entry point.

'''
from talk import Talk

import tkinter as tk
from window import Application

root = tk.Tk()
app = Application(master=root)
app.mainloop()

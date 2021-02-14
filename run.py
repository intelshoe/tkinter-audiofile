#!/usr/bin/env python3
'''
Main app entry point.

'''
import speech_recognition as sr
import time
from os import path
from talk import Talk

import tkinter as tk
from window import Application

root = tk.Tk()
app = Application(master=root)
app.mainloop()

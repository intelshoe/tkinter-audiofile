'''
This loads the tkinter application window

'''
import tkinter as tk
import speech_recognition as sr
import time
from os import path
from talk import Talk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.r = Talk()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Click me to record speech to text!"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="bottom")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print(self.r.record(5, "testing"))

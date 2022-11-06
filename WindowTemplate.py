from tkinter import *
import datetime
from tkinter import messagebox
import sqlite3
date = datetime.datetime.now().date()

conn = sqlite3.connect("bookdatabase.db")
cursor = conn.cursor()

class Window(Tk):
    def __init__(self,color="white",h=600,w=1366):
        Tk.__init__(self)
        self.color = color
        self.h = h
        self.w = w
        self.geometry(f'{w}x{h}+80+10')
        self.config(bg=self.color)
        self.iconbitmap('images\\aapicon.ico')
        self.title("LIBRARY MANAGEMENT")



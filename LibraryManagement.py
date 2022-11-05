from tkinter import *
import datetime
from tkinter import messagebox
import sqlite3
date = datetime.datetime.now().date()

conn = sqlite3.connect("bookdatabase.db")
cursor = conn.cursor()

class Book(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('1366x738+0+0')
        self.iconbitmap('images\\aapicon.ico')
        self.title("LIBRARY MANAGEMENT")
        self.frame = Frame(self, height=125, bg="light green", width=1366)
        self.frame.pack(side=TOP)
        self.resizable(0, 0)
        self.image1 = PhotoImage(file="images\\jet.png")
        self.lab1 = Label(self.frame, image=self.image1, bg="light green").place(x=320, y=0)
        self.lab2 = Label(self.frame, text="LIBRARY MANAGEMENT ", font="lucida 50 bold", bg="light green", fg="orange").place(x=450, y=20)
        self.lframe = Frame(self, height=612, width=1366, bg="green")
        self.lframe.pack(side=BOTTOM)
        self.lframe.place(x=0, y=125)
        self.bview = Button(self.lframe, text="\t\tView All Book\t\t\t", command=self.view_lib, bg="white", fg="green", font="lucida 15 bold", )
        self.bview.place(x=400, y=30)
        self.badd = Button(self.lframe, text="\t\tAdd Book\t\t\t", command=self.add_book, bg="white", fg="green", font="lucida 15 bold", )
        self.badd.place(x=400, y=100)
        self.bdel = Button(self.lframe, text="\t\tDelete Book\t\t\t", command=self.del_book, bg="white", fg="green", font="lucida 15 bold", )
        self.bdel.place(x=400, y=160)
        self.bprc = Button(self.lframe, text="\t\tFind Book's Price or Author\t\t", command=self.book_prc, bg="white", fg="green", font="lucida 15 bold", )
        self.bprc.place(x=400, y=220)
        self.bentr = Button(self.lframe, text="\t\tEntry of student\t\t\t", command=self.studetn, bg="white", fg="green", font="lucida 15 bold", )
        self.bentr.place(x=400, y=280)
        self.bback = Button(self.lframe, text="\t\tExit\t\t\t\t", command=self.exet, bg="white", fg="green", font="lucida 15 bold", )
        self.bback.place(x=400, y=340)
    def view_lib(self):
        print("viewing the library")
    def add_book(self):
           print("adding the book")
    def del_book(self):
        print("deleting the book")
    def book_prc(self):
        print("getting book's price and author")
    def studetn(self):
        print("entering the student's data")
    def exet(self):
        print("exiting the program")


if __name__ == "__main__":
    b1 = Book().mainloop()
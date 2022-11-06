from tkinter import *
import datetime
from tkinter import messagebox
import sqlite3
from WindowTemplate import Window as win
date = datetime.datetime.now().date()

conn = sqlite3.connect("bookdatabase.db")
cursor = conn.cursor()

class Library():
    def __init__(self):
        self.h = 600
        self.w = 1366
        self.mainwin = win("green")
        self.tframe = Frame(self.mainwin, height=125, bg="light green", width=1366)
        self.tframe.pack(side=TOP)
        self.image1 = PhotoImage(file="images\\jet.png")
        self.lab1 = Label(self.tframe, image=self.image1, bg="light green").place(x=320, y=0)
        self.lab2 = Label(self.tframe, text="LIBRARY MANAGEMENT ", font="lucida 50 bold", bg="light green", fg="orange").place(x=450, y=20)
        self.bframe = Frame(self.mainwin, height=600, width=1366, bg="green")
        self.bframe.pack(side=BOTTOM)
        self.bview = Button(self.bframe, text="\t\tView All Book\t\t\t", command=self.view_lib, bg="white", fg="green", font="lucida 15 bold", )
        self.bview.place(x=400, y=30)
        self.badd = Button(self.bframe, text="\t\tAdd Book\t\t\t", command=self.add_book, bg="white", fg="green", font="lucida 15 bold", )
        self.badd.place(x=400, y=100)
        self.bdel = Button(self.bframe, text="\t\tDelete Book\t\t\t", command=self.del_book, bg="white", fg="green", font="lucida 15 bold", )
        self.bdel.place(x=400, y=160)
        self.bprc = Button(self.bframe, text="\t\tFind Book's Price or Author\t\t", command=self.book_prc, bg="white", fg="green", font="lucida 15 bold", )
        self.bprc.place(x=400, y=220)
        self.bentr = Button(self.bframe, text="\t\tEntry of student\t\t\t", command=self.studetn, bg="white", fg="green", font="lucida 15 bold", )
        self.bentr.place(x=400, y=280)
        self.bback = Button(self.bframe, text="\t\tExit\t\t\t\t", command=self.exet, bg="white", fg="green", font="lucida 15 bold", )
        self.bback.place(x=400, y=340)




    def view_lib(self):
        print("viewing the library")
        self.mainwin.destroy()
        self.viewwin = win("light blue")
        self.viewFrame = Frame(self.viewwin,height=0,width = self.w).pack()
        def back():
            print("Exiting the View Library")
            self.viewwin.destroy()
            main()
        self.bbtn = Button(self.viewFrame,text = "Back",bg = "red",fg = "green",command=back)
        self.bbtn.pack()
            
    def add_book(self):
        print("adding the book")
        self.mainwin.destroy()
        self.addBookwin = win("green")
        self.addBookFrame = Frame(self.addBookwin,height=0,width = self.w).pack()
        def back():
            print("Exiting the Adding Book")
            self.addBookwin.destroy()
            main()
        self.bbtn = Button(self.addBookFrame,text = "Back",bg = "red",fg = "green",command=back)
        self.bbtn.pack()
        
    def del_book(self):
        print("deleting the book")
        self.mainwin.destroy()
        self.delBookwin = win("black")
        self.delBookFrame = Frame(self.delBookwin,height=0,width = self.w).pack()
        def back():
            print("Exiting the deleting Book")
            self.delBookwin.destroy()
            main()
        self.bbtn = Button(self.delBookFrame,text = "Back",bg = "red",fg = "green",command=back)
        self.bbtn.pack()


    def book_prc(self):
        print("getting book's price and author")
        self.mainwin.destroy()
        self.authPrcwin = win("red")
        self.authPrcFrame = Frame(self.authPrcwin,height=0,width = self.w).pack()
        def back():
            print("Exiting the author and price")
            self.authPrcwin.destroy()
            main()
        self.bbtn = Button(self.authPrcFrame,text = "Back",bg = "red",fg = "green",command=back)
        self.bbtn.pack()

    def studetn(self):
        print("entering the student's data")
        self.mainwin.destroy()
        self.studwin = win("blue")
        self.studFrame = Frame(self.studwin,height=0,width = self.w).pack()
        def back():
            print("Exiting the Student entry")
            self.studwin.destroy()
            main()
        self.bbtn = Button(self.studFrame,text = "Back",bg = "red",fg = "green",command=back)
        self.bbtn.pack()

    def exet(self):
        print("exiting the program")
        self.mainwin.destroy()


def main():
    l = Library()
    l.mainwin.mainloop()


if __name__ == "__main__":
    main()
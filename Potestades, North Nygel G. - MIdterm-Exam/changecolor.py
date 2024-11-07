from tkinter import *
from tkinter import messagebox


class MyWindow:
    def __init__(self, win):
        self.win = win
        self.button = Button(self.win, text="Click to Change Color", command=self.changecolor)
        self.button.place(x=90, y=100)

    def changecolor(self):
        self.button = Button(self.win, text="Click to Change Color", command=self.changecolor, bg='Yellow')
        self.button.place(x=90, y=100)

if __name__ == "__main__":
    window = Tk()
    mywin = MyWindow(window)
    window.geometry("300x250+10+10")
    window.title("Special Midterm Exam in OOP")
    window.mainloop()
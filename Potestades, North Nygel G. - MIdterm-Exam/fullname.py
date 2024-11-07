from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.win = win
        self.lbl1 = Label(self.win, text="Enter your fullname", fg="Red")
        self.lbl1.place(x=40, y=100)
        self.entry1 = Entry(self.win, width=20, font=30)
        self.entry1.place(x=270, y=100)
        self.button = Button(self.win, text="Click to display your Fullname", fg="Red", command=self.display)
        self.button.place(x=40, y=150)
        self.entry2 = Entry(self.win, width=20, font=30)
        self.entry2.place(x=270, y=150)

    def display(self):
        self.entry2.delete(0, 'end')
        self.entry2.insert(END, str(self.entry1.get()))


if __name__ == "__main__":
    window = Tk()
    mywin = MyWindow(window)
    window.geometry("500x300+10+10")
    window.title("Midterm in OOP")
    window.mainloop()
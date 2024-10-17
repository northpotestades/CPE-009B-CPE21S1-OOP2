from tkinter import *
from registration import MyWindow

if __name__ == "__main__":
    window = Tk()
    mywin = MyWindow(window)
    window.geometry("400x300+10+10")
    window.title("Account Registration System")
    window.mainloop()
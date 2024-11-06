from tkinter import *
import math


def write(filepath, data):
    with open(filepath, 'a') as write_file:
        for key, value in data.items():
            write_file.write('%s:%s\n' % (key, value))


class MyWindow:
    def __init__(self, win):
        win.configure(bg='#ffeadc')
        self.lbl1 = Label(win, text='Simple Calculator', fg="#00008b", font=('Arial', 10, "bold"), bg='#ffeadc')
        self.lbl1.place(x=95,y=20)
        self.lbl2 = Label(win, text='1st Number', fg="#00008b", bg='#ffeadc')
        self.lbl2.place(x=30, y=60)
        self.t2 = Entry(win, bd=2)
        self.t2.place(x=130, y=60)
        self.lbl3 = Label(win, text='2nd Number', fg="#00008b", bg='#ffeadc')
        self.lbl3.place(x=30, y=100)
        self.t3 = Entry(win, bd=2)
        self.t3.place(x=130, y=100)
        self.lbl4 = Label(win, text='Result', fg="#00008b", bg='#ffeadc')
        self.lbl4.place(x=30, y=140)
        self.t4 = Entry(win, bd=2)
        self.t4.place(x=130, y=140)
        self.btn1 = Button(win, text='Add', command=self.add, bd=2, fg="#00008b", bg='#ffb684')
        self.btn1.place(x=90,y=180)
        self.btn2 = Button(win, text='Sub', command=self.sub, bd=2, fg="#00008b", bg='#ffb684')
        self.btn2.place(x=170, y=180)
        self.btn3 = Button(win, text='Mul', command=self.mul, bd=2, fg="#00008b", bg='#ffb684')
        self.btn3.place(x=90, y=230)
        self.btn4 = Button(win, text='Div', command=self.div, bd=2, fg="#00008b", bg='#ffb684')
        self.btn4.place(x=170, y=230)
        self.btn5 = Button(win, text='Clear', command=self.clear, bd=2, fg="#00008b", bg='#ffd5b9')
        self.btn5.place(x=250, y=260)

    def add(self):
        self.t4.delete(0,'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result=num1+num2
        self.t4.insert(END, str(result))

    def sub(self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result=num1-num2
        self.t4.insert(END, str(result))

    def mul(self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result=num1*num2
        self.t4.insert(END, str(result))

    def div(self):
        self.t4.delete(0, 'end')
        num1 = int(self.t2.get())
        num2 = int(self.t3.get())
        result=num1/num2
        self.t4.insert(END, str(result))

    def clear(self):
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')


window = Tk()
mywin = MyWindow(window)
window.geometry("300x300+10+10")
window.title("Simple Calculator")
window.mainloop()
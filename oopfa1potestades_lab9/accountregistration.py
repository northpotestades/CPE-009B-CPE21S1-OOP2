from tkinter import *
from tkinter import messagebox


def write(filepath, data):
    with open(filepath, 'a') as write_file:
        for key, value in data.items():
            write_file.write('%s:%s\n' % (key, value))


class MyWindow:
    def __init__(self, win):
        win.configure(bg='#ffeadc')
        self.win = win
        self.lbl1 = Label(self.win, text="Account Registration System", fg="#00008b", font=("Arial", 16), bg='#ffeadc')
        self.lbl1.place(x=65, y=10)
        self.lbl2 = Label(self.win, text="First Name", fg="#00008b", bg='#ffeadc')
        self.lbl2.place(x=40, y=50)
        self.entry1 = Entry(self.win, width=35, fg="#00008b", bg='#ffb684')
        self.entry1.place(x=145, y=50)
        self.lbl3 = Label(self.win, text="Last Name", fg="#00008b", bg='#ffeadc')
        self.lbl3.place(x=40, y=80)
        self.entry2 = Entry(self.win, width=35, fg="#00008b", bg='#ffb684')
        self.entry2.place(x=145, y=80)
        self.lbl4 = Label(self.win, text="Username", fg="#00008b", bg='#ffeadc')
        self.lbl4.place(x=40, y=110)
        self.entry3 = Entry(self.win, width=35, fg="#00008b", bg='#ffb684')
        self.entry3.place(x=145, y=110)
        self.lbl5 = Label(self.win, text="Password", fg="#00008b", bg='#ffeadc')
        self.lbl5.place(x=40, y=140)
        self.entry4 = Entry(self.win, show="*", width=35, fg="#00008b", bg='#ffb684')
        self.entry4.place(x=145, y=140)
        self.lbl6 = Label(self.win, text="Email Address", fg="#00008b", bg='#ffeadc')
        self.lbl6.place(x=40, y=170)
        self.entry5 = Entry(self.win, width=35, fg="#00008b", bg='#ffb684')
        self.entry5.place(x=145, y=170)
        self.lbl7 = Label(self.win, text="Contact Number", fg="#00008b", bg='#ffeadc')
        self.lbl7.place(x=40, y=200)
        self.entry6 = Entry(self.win, width=35, fg="#00008b", bg='#ffb684')
        self.entry6.place(x=145, y=200)
        self.btn1 = Button(self.win, text="Submit", fg="#00008b", command=self.submit, bg='#ffb684')
        self.btn1.place(x=100, y=240)
        self.btn2 = Button(self.win, text="Clear", fg="#00008b", command=self.clear, bg='#ffb684')
        self.btn2.place(x=250, y=240)

    def submit(self):
        if self.entry1.index("end") == 0 or self.entry2.index("end") == 0 or self.entry3.index("end") == 0 or self.entry4.index("end") == 0 or self.entry5.index("end") == 0 or self.entry6.index("end") == 0:
            messagebox.showinfo("Not Submitted", "Invalid! One or more fields are empty.")
            return
        else:
            data = {label: entry for label, entry in
                    zip(["First Name", "Last Name", "Username", "Password", "Email Address", "Contact Number"],
                        [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(),
                         self.entry5.get(), self.entry6.get()])}
            messagebox.showinfo("Submitted", f"Registration Data: {data}")
            write(data=data, filepath="Database.txt")

    def clear(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry5.delete(0, 'end')
        self.entry6.delete(0, 'end')

if __name__ == "__main__":
    window = Tk()
    mywin = MyWindow(window)
    window.geometry("400x300+10+10")
    window.title("Account Registration System")
    window.mainloop()
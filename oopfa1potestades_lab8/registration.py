import tkinter as tk
from tkinter import messagebox


class MyWindow:
    def __init__(self, win):
        self.win = win
        self.win.title("Account Registration")

        window_width = 400
        window_height = 300
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.create_widgets()

    def create_widgets(self):
        lbl1 = tk.Label(self.win, text="Account Registration System", font=("Arial", 16))
        lbl1.place(x=50, y=10)

        labels = ["First Name", "Last Name", "Username", "Password", "Email Address", "Contact Number"]
        self.entries = []

        for i, label in enumerate(labels):
            lbl = tk.Label(self.win, text=label)
            lbl.place(x=50, y=50 + i * 30)
            entry = tk.Entry(self.win)
            entry.place(x=180, y=50 + i * 30)
            self.entries.append(entry)

        btn1 = tk.Button(self.win, text="Submit", command=self.submit)
        btn1.place(x=100, y=220)

        btn2 = tk.Button(self.win, text="Clear", command=self.clear)
        btn2.place(x=250, y=220)

    def submit(self):
        data = {label: entry.get() for label, entry in
                zip(["First Name", "Last Name", "Username", "Password", "Email Address", "Contact Number"],
                    self.entries)}
        messagebox.showinfo("Submitted", f"Registration Data: {data}")

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
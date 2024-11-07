from tkinter import *
from tkinter import messagebox
import math


def calculate_result(operation):
    try:
        if "sin" in operation:
            num = float(operation.replace("sin", "").strip())
            return math.sin(num)  # Convert degrees to radians
        elif "cos" in operation:
            num = float(operation.replace("cos", "").strip())
            return math.cos(num)  # Convert degrees to radians
        elif "exp" in operation:
            num = float(operation.replace("exp", "").strip())
            return math.exp(num)
        else:
            return eval(operation)
    except Exception as e:
        raise e


def save_to_file(text):
    try:
        with open("calculator_history.txt", "a") as file:
            file.write(text)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to save to file: {str(e)}")


class MyWindow:
    def __init__(self, win):
        self.win = win
        self.menu_bar = Menu(win)
        self.win.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Clear", command=self.clear)
        self.file_menu.add_command(label="Load Last Operation", command=self.load_operations)
        self.file_menu.add_command(label="Exit", command=self.exit_program)
        self.file_menu.add_separator()

        self.entry = Entry(win, width=20, font=("Arial", 16), borderwidth=2, relief="solid", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.operation = ""

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("sin", 5, 1), ("cos", 5, 2), ("exp", 5, 3)
        ]

        for (text, row, col) in buttons:
            button = Button(win, text=text, width=5, height=2, font=("Arial", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.win.bind("<Control-q>", self.exit_program)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = calculate_result(self.operation)
                self.entry.delete(0, END)
                self.entry.insert(END, result)
                save_to_file(f"{self.operation} = {result}\n")
                self.operation = str(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid operation: {str(e)}")
                self.operation = ""
                self.entry.delete(0, END)
        elif text == "C":
            self.operation = ""
            self.entry.delete(0, END)
        else:
            self.operation += str(text)
            self.entry.delete(0, END)
            self.entry.insert(END, self.operation)

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.win.quit()

    def clear(self):
        self.operation = ""
        self.entry.delete(0, END)

    def load_operations(self):
        try:
            with open("calculator_history.txt", "r") as file:
                history = file.readlines()
                self.entry.insert(END, history[-1])
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load history: {str(e)}")
            return []

if __name__ == "__main__":
    window = Tk()
    mywin = MyWindow(window)
    window.title("Calculator")
    window.geometry("300x400")
    window.mainloop()
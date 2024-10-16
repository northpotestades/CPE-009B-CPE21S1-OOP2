import tkinter as tk
from registration import MyWindow

if __name__ == "__main__":
    window = tk.Tk()
    app = MyWindow(window)
    window.mainloop()
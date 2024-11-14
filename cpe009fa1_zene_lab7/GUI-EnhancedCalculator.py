import tkinter as tk
from tkinter import ttk
import math

# Functions for calculation
def add():
    result.set(float(entry1.get()) + float(entry2.get()))
    history.insert(tk.END, f"{entry1.get()} + {entry2.get()} = {result.get()}\n")

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))
    history.insert(tk.END, f"{entry1.get()} - {entry2.get()} = {result.get()}\n")

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))
    history.insert(tk.END, f"{entry1.get()} * {entry2.get()} = {result.get()}\n")

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
        history.insert(tk.END, f"{entry1.get()} / {entry2.get()} = {result.get()}\n")
    except ZeroDivisionError:
        result.set("Error! Division by zero.")
        history.insert(tk.END, f"Division by zero error\n")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")
    history.delete(1.0, tk.END)

# Advanced operations
def square_root():
    result.set(math.sqrt(float(entry1.get())))
    history.insert(tk.END, f"sqrt({entry1.get()}) = {result.get()}\n")

def power():
    result.set(math.pow(float(entry1.get()), float(entry2.get())))
    history.insert(tk.END, f"{entry1.get()} ^ {entry2.get()} = {result.get()}\n")

# Create the main window
root = tk.Tk()
root.title("Enhanced Calculator")

# Create StringVar to hold the result
result = tk.StringVar()

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="Gray")
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TEntry", font=("Helvetica", 14), background="Gray")
style.configure("TFrame", background="Gray")
root.config(bg="#1c1c1c")

# Create the layout
mainframe = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(mainframe, text="Enter first number:", style="TLabel").grid(row=0, column=0, padx=5, pady=5)
entry1 = ttk.Entry(mainframe, style="TEntry")
entry1.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(mainframe, text="Enter second number:", style="TLabel").grid(row=1, column=0, padx=5, pady=5)
entry2 = ttk.Entry(mainframe, style="TEntry")
entry2.grid(row=1, column=1, padx=5, pady=5)

# Buttons for operations
ttk.Button(mainframe, text="Add", command=add, style="TButton").grid(row=2, column=0, padx=5, pady=5)
ttk.Button(mainframe, text="Subtract", command=subtract, style="TButton").grid(row=2, column=1, padx=5, pady=5)
ttk.Button(mainframe, text="Multiply", command=multiply, style="TButton").grid(row=3, column=0, padx=5, pady=5)
ttk.Button(mainframe, text="Divide", command=divide, style="TButton").grid(row=3, column=1, padx=5, pady=5)
ttk.Button(mainframe, text="Square Root", command=square_root, style="TButton").grid(row=4, column=0, padx=5, pady=5)
ttk.Button(mainframe, text="Power", command=power, style="TButton").grid(row=4, column=1, padx=5, pady=5)

# Label to show result
ttk.Label(mainframe, text="Result:", style="TLabel").grid(row=5, column=0, padx=5, pady=5)
result_label = ttk.Label(mainframe, textvariable=result, style="TLabel")
result_label.grid(row=5, column=1, padx=5, pady=5)

# Clear button
ttk.Button(mainframe, text="Clear", command=clear, style="TButton").grid(row=6, column=0, padx=5, pady=5)

# History
ttk.Label(mainframe, text="History:", style="TLabel").grid(row=7, column=0, padx=5, pady=5)
history = tk.Text(mainframe, height=10, width=30, font=("Helvetica", 12), bg="#f0f0f0", wrap=tk.WORD)
history.grid(row=7, column=1, padx=5, pady=5)

# Input validation
def validate_entry(char):
    return char.isdigit() or char == '.' or char == '-'

vcmd = (root.register(validate_entry), '%S')
entry1.config(validate='key', validatecommand=vcmd)
entry2.config(validate='key', validatecommand=vcmd)

# Start the main loop
root.mainloop()





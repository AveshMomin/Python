import tkinter as tk
from tkinter import ttk

def convert_length():
    try:
        value = float(entry.get())
        if unit_var.get() == "Feet to Meters":
            result = value * 0.3048
        elif unit_var.get() == "Meters to Feet":
            result = value * 3.28084
        elif unit_var.get() == "Inches to Centimeters":
            result = value * 2.54
        elif unit_var.get() == "Centimeters to Inches":
            result = value * 0.393701
        else:
            result = "Invalid conversion"
        result_label.config(text=f"{result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Unit Converter")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=10, font=('Arial', 12))
style.configure("TLabel", font=('Arial', 12))

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

entry = ttk.Entry(frame, font=('Arial', 12), width=10)
entry.pack(side=tk.LEFT, padx=5)

unit_options = ["Feet to Meters", "Meters to Feet", "Inches to Centimeters", "Centimeters to Inches"]
unit_var = tk.StringVar(value=unit_options[0])

unit_menu = ttk.OptionMenu(frame, unit_var, *unit_options)
unit_menu.pack(side=tk.LEFT, padx=5)

convert_button = ttk.Button(root, text="Convert", command=convert_length)
convert_button.pack(pady=10)

result_label = ttk.Label(root, text="", font=('Arial', 14, 'bold'))
result_label.pack()

root.mainloop()

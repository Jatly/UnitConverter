import tkinter as tk
from tkinter import ttk

# Conversion function
def convert():
    try:
        input_value = float(entry.get())
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()

        if not from_unit or not to_unit:
            result.set("Select valid units!")
            return

        # Conversion logic
        category = category_combobox.get()
        if category == "Length":
            conversion_factors = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084}
            result_value = input_value * conversion_factors[to_unit] / conversion_factors[from_unit]
        elif category == "Weight":
            conversion_factors = {"Kilograms": 1, "Pounds": 2.20462, "Grams": 1000, "Ounces": 35.274}
            result_value = input_value * conversion_factors[to_unit] / conversion_factors[from_unit]
        elif category == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result_value = (input_value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result_value = (input_value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result_value = input_value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result_value = input_value - 273.15
            elif from_unit == to_unit:
                result_value = input_value
            else:
                result.set("Invalid conversion!")
                return
        elif category == "Time":
            conversion_factors = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400}
            result_value = input_value * conversion_factors[to_unit] / conversion_factors[from_unit]
        elif category == "Currency":
            # Sample conversion rates (e.g., to USD)
            conversion_factors = {"USD": 1, "EUR": 0.85, "INR": 82.5, "JPY": 110}
            result_value = input_value * conversion_factors[to_unit] / conversion_factors[from_unit]
        else:
            result.set("Invalid category!")
            return

        # Display result
        result.set(f"{result_value:.2f}")
    except ValueError:
        result.set("Invalid input!")

# Update units based on selected category
def update_units(event=None):
    category = category_combobox.get()
    if category == "Length":
        units = ["Meters", "Kilometers", "Miles", "Feet"]
    elif category == "Weight":
        units = ["Kilograms", "Pounds", "Grams", "Ounces"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    elif category == "Time":
        units = ["Seconds", "Minutes", "Hours", "Days"]
    elif category == "Currency":
        units = ["USD", "EUR", "INR", "JPY"]
    else:
        units = []

    from_unit_combobox['values'] = units
    to_unit_combobox['values'] = units
    if units:
        from_unit_combobox.current(0)
        to_unit_combobox.current(1)

# Button hover effect
def on_enter(event):
    event.widget.configure(style="Hover.TButton")

def on_leave(event):
    event.widget.configure(style="Dark.TButton")

# Initialize main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x450")
root.resizable(False, False)

# Dark theme styling
style = ttk.Style()
root.configure(bg="#1e1e1e")  # Set dark background
style.theme_use("clam")

# Global styles
style.configure("TLabel", font=("Arial", 12), background="#1e1e1e", foreground="#ffffff")
style.configure("TCombobox", font=("Arial", 12), fieldbackground="#333333", background="#333333", foreground="#00000")
style.configure("TEntry", font=("Arial", 12), fieldbackground="#333333", foreground="#ffffff")
style.configure("Dark.TButton", font=("Arial", 12), background="#333333", foreground="#ffffff", borderwidth=0)
style.configure("Hover.TButton", font=("Arial", 12), background="#555555", foreground="#ffffff", borderwidth=0)
style.map("Dark.TButton", background=[("pressed", "#777777")])

# Dropdown for categories
ttk.Label(root, text="Select Category:").pack(pady=5)
category_combobox = ttk.Combobox(root, values=["Length", "Weight", "Temperature", "Time", "Currency"], state="readonly", style="TCombobox")
category_combobox.current(0)
category_combobox.pack(pady=5)
category_combobox.bind("<<ComboboxSelected>>", update_units)

# Input field
ttk.Label(root, text="Enter Value:").pack(pady=5)
entry = ttk.Entry(root, style="TEntry", justify="center")
entry.pack(pady=5)

# From and To unit dropdowns
ttk.Label(root, text="From:").pack(pady=5)
from_unit_combobox = ttk.Combobox(root, state="readonly", style="TCombobox")
from_unit_combobox.pack(pady=5)

ttk.Label(root, text="To:").pack(pady=5)
to_unit_combobox = ttk.Combobox(root, state="readonly", style="TCombobox")
to_unit_combobox.pack(pady=5)

# Result display
result = tk.StringVar()
ttk.Label(root, text="Converted Value:").pack(pady=5)
result_label = ttk.Label(root, textvariable=result, font=("Arial", 14, "bold"), foreground="#ffffff", anchor="center")
result_label.pack(pady=5, ipadx=10, ipady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert, style="Dark.TButton")
convert_button.pack(pady=10)
convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

# Initialize with default category
update_units()

# Run the application
root.mainloop()

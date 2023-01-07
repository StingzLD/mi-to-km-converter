from tkinter import *


# Create button action
def calculate_mi_to_km():
    miles = int(entry.get())
    km = miles * 1.609344
    result.config(text=km)


DEFAULT_PADDING = {"padx": 10, "pady": 10}

# Window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# Entry field
entry = Entry(width=20)
entry.grid(column=1, row=0)

# "Miles" label
mi_label = Label(text="Miles")
mi_label.grid(column=2, row=0)
mi_label.config(DEFAULT_PADDING)

# "is equal to" label
iet_label = Label(text="is equal to")
iet_label.grid(column=0, row=1)
iet_label.config(DEFAULT_PADDING)

# Result label
result = Label(text="0")
result.grid(column=1, row=1)
result.config(DEFAULT_PADDING)

# "Kilometers" label
km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)
km_label.config(DEFAULT_PADDING)

# Calculate button
button = Button(text="Calculate", command=calculate_mi_to_km)
button.grid(column=1, row=2)

window.mainloop()

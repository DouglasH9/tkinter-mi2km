from tkinter import *


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(300, 300)
window.config(padx=30, pady=30)


def calculate():
    miles = float(miles_input.get())
    kilometers = miles * 1.61
    result_label["text"] = kilometers


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
input_label = Label(text="Miles", font=("Roboto Mono", 24, "bold"))
input_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to", font=("Roboto Mono", 24, "bold"))
is_equal_label.grid(column=0, row=1)
result_label = Label(text="0", font=("Roboto Mono", 24, "bold"))
result_label.grid(column=1, row=1)
km_label = Label(text="Km", font=("Roboto Mono", 24, "bold"))
km_label.grid(column=2, row=1)
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()


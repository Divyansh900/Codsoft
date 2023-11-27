# DAY 5
# PASSWORD GENERATOR

import tkinter as tk
import random

app = tk.Tk()
app.title("PASSWORD GENERATOR")
lee = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y',
       'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
       'V', 'W', 'X', 'Y', 'Z']
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

field_points = ['Lenght', 'Numbers', 'Symbols']

for i, field in enumerate(field_points):
    label = tk.Label(app, text=f"{field_points[i]} : ")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

lenght = tk.Entry(app)
lenght.grid(row=0, column=1, padx=10, pady=5, sticky="w")

number = tk.Entry(app)
number.grid(row=1, column=1, padx=10, pady=5, sticky="w")

symbols = tk.Entry(app)
symbols.grid(row=2, column=1, padx=10, pady=5, sticky="w")

passw = tk.Entry(app,bg = "Black", fg = "white")
passw.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
arr = ""


def gen():
    global arr
    arr = ""
    leng = int(lenght.get())
    numbers = int(number.get())
    symbol = int(symbols.get())
    extra = numbers + symbol

    for l in range(0, leng):
        if l < leng - extra:
            arr += random.choice(lee)

        elif l < leng - symbol:
            arr += random.choice(n)

        elif l < leng:
            arr += random.choice(s)

    arr = "".join(random.sample(arr, len(arr)))
    passw.insert(0, arr)


# print(f"\nThe password is : {arr}\n")


b_gen = tk.Button(app, height=2, width=18,  text="Generate Password", command=gen)
b_gen.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

app.mainloop()

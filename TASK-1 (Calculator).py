import tkinter as tk

root = tk.Tk()
root.title("Calculator")

inp = tk.Entry(root, width=12, font=("Arial", 20), bg="gray20", fg="white")
inp.grid(row=0, column=0, columnspan=4)


def b_click(num):
    current = inp.get()
    inp.delete(0, tk.END)
    inp.insert(0, current + str(num))


def b_clear():
    inp.delete(0, tk.END)


def b_add():
    current = inp.get()
    global num1, op
    op = "addition"
    num1 = float(current)
    inp.delete(0, tk.END)


def b_sub():
    current = inp.get()
    global num1, op
    op = "subtraction"
    num1 = float(current)
    inp.delete(0, tk.END)


def b_mult():
    current = inp.get()
    global num1, op
    op = "multiplication"
    num1 = float(current)
    inp.delete(0, tk.END)


def b_div():
    current = inp.get()
    global num1, op
    op = "division"
    num1 = float(current)
    inp.delete(0, tk.END)


def b_equal():
    num2 = float(inp.get())
    inp.delete(0, tk.END)
    result = 0
    if op == "addition":
        result = num1 + num2
    elif op == "subtraction":
        result = num1 - num2
    elif op == "multiplication":
        result = num1 * num2
    elif op == "division":
        if num2 == 0:
            result = "Error, division by zero not allowed"
        else:
            result = num1 / num2

    inp.insert(0, result)


# Create number buttons
button_1 = tk.Button(root, width=5, height=3, bg="gray80", text="1", command=lambda: b_click(1))
button_2 = tk.Button(root, width=5, height=3, bg="gray80", text="2", command=lambda: b_click(2))
button_3 = tk.Button(root, width=5, height=3, bg="gray80", text="3", command=lambda: b_click(3))
button_4 = tk.Button(root, width=5, height=3, bg="gray80", text="4", command=lambda: b_click(4))
button_5 = tk.Button(root, width=5, height=3, bg="gray80", text="5", command=lambda: b_click(5))
button_6 = tk.Button(root, width=5, height=3, bg="gray80", text="6", command=lambda: b_click(6))
button_7 = tk.Button(root, width=5, height=3, bg="gray80", text="7", command=lambda: b_click(7))
button_8 = tk.Button(root, width=5, height=3, bg="gray80", text="8", command=lambda: b_click(8))
button_9 = tk.Button(root, width=5, height=3, bg="gray80", text="9", command=lambda: b_click(9))
button_0 = tk.Button(root, width=5, height=3, bg="gray80", text="0", command=lambda: b_click(0))

# Create operator buttons
button_add = tk.Button(root, width=5, height=3, bg="gray80", text="+", command=b_add)
button_subtract = tk.Button(root, width=5, height=3, bg="gray80", text="-", command=b_sub)
button_multiply = tk.Button(root, width=5, height=3, bg="gray80", text="*", command=b_mult)
button_divide = tk.Button(root, width=5, height=3, bg="gray80", text="/", command=b_div)

# Create equal and clear buttons
button_equal = tk.Button(root, width=5, height=3, bg="gray80", text="=", command=b_equal)
button_clear = tk.Button(root, width=5, height=3, bg="gray80", text="C", command=b_clear)

# Place the buttons in the grid layout
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

# Start the main application loop
root.mainloop()

# calc_v3.py
import tkinter as tk


def click_button(item):
    current_text = expression_field.get()
    expression_field.delete(0, tk.END)
    expression_field.insert(0, current_text + str(item))


def clear_field():
    expression_field.delete(0, tk.END)


def calculate():
    try:
        result = str(eval(expression_field.get()))
        expression_field.delete(0, tk.END)
        expression_field.insert(0, result)
    except:
        expression_field.delete(0, tk.END)
        expression_field.insert(0, "Error")


# Main Window setup
window = tk.Tk()
window.title("My Python Calculator")
window.geometry("300x400")

expression_field = tk.Entry(window, font=('Arial', 24))
expression_field.pack(pady=10, fill=tk.X)

# Button Frame
buttons_frame = tk.Frame(window)
buttons_frame.pack()

# Button Layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 0
col_val = 0

for button in buttons:
    def action(x=button): return click_button(x)
    if button == "C":
        action = clear_field
    elif button == "=":
        action = calculate

    tk.Button(buttons_frame, text=button, width=5, height=2,
              command=action).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
